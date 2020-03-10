import sys


def main_file_data_reader(file):
    read_lines: int = 0
    read_word: int = 0
    read_bytes: int = 0
    max_line_length: int = 0

    file_data = open(file, "r")
    for line in file_data:
        read_lines += 1
        if len(line) > max_line_length:
            max_line_length = len(line)
        read_bytes += len(bytes(line, 'utf-8'))
        read_word += len(line.split(' '))

    file_data.close()
    print("Bytes : ", read_bytes, "\nWords : ", read_word, "\nLines : ", read_lines,
          "\nMax line length : ", max_line_length)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing file input")
        exit(1)

    main_file_data_reader(sys.argv[0])
