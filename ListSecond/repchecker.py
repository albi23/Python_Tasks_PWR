import hashlib
import os
import sys


class FileDataCollector:
    def __init__(self, location, occurrences):
        self.occurrences = occurrences
        self.location = location

    def __str__(self):
        return '{occurrences :' + str(self.occurrences) + ',location :' + self.location + ' }'

    def __hash__(self):
        return hash((self.occurrences, self.location))

    def __eq__(self, other):
        return (self.occurrences, self.location) == (other.occurrences, other.location)

    def __ne__(self, other):
        return not (self == other)

    def increase_occurrences(self):
        self.occurrences += 1

    def append_location(self, next_location: str):
        self.location += '\n' + next_location

    def get_location(self) -> str:
        return self.location

    def get_occurrences(self) -> int:
        return self.occurrences


class FileKeyMap:
    def __init__(self, hash_sum, size):
        self.hash_sum = hash_sum
        self.size = size

    def __hash__(self):
        return hash((self.hash_sum, self.size))

    def __eq__(self, other):
        return (self.hash_sum, self.size) == (other.hash_sum, other.size)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '{hash_sum :' + str(self.hash_sum) + ',size :' + str(self.size) + ' }'


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


def run_walk(path: str):
    file_tree_map = {}
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            file_full_path = os.path.join(root, name)
            file_size = os.path.getsize(file_full_path)
            md5sum_hash = md5sum(file_full_path)
            map_key = FileKeyMap(md5sum_hash, file_size)
            if file_tree_map.get(map_key) is None:
                file_tree_map[map_key] = FileDataCollector(file_full_path, 1)
            else:
                file_data_collector: FileDataCollector = file_tree_map.get(map_key)
                file_data_collector.increase_occurrences()
                file_data_collector.append_location(file_full_path)

    for map_key, values in file_tree_map.items():
        if values.get_occurrences() > 1:
            print(values.get_location() + "\n".ljust(40, '-'))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python repchecker.py path")
        exit(1)
    run_walk(sys.argv[1])
