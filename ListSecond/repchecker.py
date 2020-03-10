import hashlib
import os
import sys

file_tree_data = {}


class FileDataCollector:
    def __init__(self, location, occurrences):
        self.occurrences = occurrences
        self.location = location

    def increase_occurrences(self):
        self.occurrences += 1


class FileKeyMap:
    def __init__(self, hash_sum, size):
        self.hash_sum = hash_sum
        self.size = size

    def __hash__(self):
        return hash((self.hash_sum, self.size))

    def __eq__(self, other):
        return (self.hash_sum, self.size) == (other.name, other.location)

    def __ne__(self, other):
        return not (self == other)


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


def run_walk(path: str):
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            file_full_name = os.path.join(root, name)
            file_size = os.path.getsize(file_full_name)
            md5sum_hash = md5sum(file_full_name)
            if file_tree_data.get(FileKeyMap(md5sum_hash, file_size)) is not None:
                file_data_collector: FileDataCollector = file_tree_data.get(FileKeyMap(md5sum_hash, file_size))
                file_data_collector.increase_occurrences()
            else:
                key = FileKeyMap(md5sum_hash, file_size)
                value = FileDataCollector(file_full_name, 1)
                file_tree_data[key] = value
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    print(file_tree_data)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing path input ")
        exit(1)
    run_walk(sys.argv[1])
