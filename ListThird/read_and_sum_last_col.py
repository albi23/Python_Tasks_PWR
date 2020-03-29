import sys


def sum_files_size(file_name: str) -> int:
    with open(file_name, "r") as file:
        return sum(int(line.split()[-1]) for line in file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python transposition.py file")
        print("Note:  last column in file must contains file size info")
        exit(1)

    print(sum_files_size(sys.argv[1]))
