import sys
from typing import List


def gen_matrix(matrix_size: int) -> List[str]:
    if matrix_size < 1:
        return []
    return [" ".join([str(step + nth_value) + "." + str(step + nth_value) for step in range(1, matrix_size + 1, 1)]) for nth_value in
            range(0, matrix_size * matrix_size, matrix_size)]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python transposition.py matrix_size")
        exit(1)

    matrix = gen_matrix(int(sys.argv[1]))
    print("before transposition : ", matrix)
    transposed = [" ".join([matrix[index].split()[line_index] for index in range(0, len(matrix))]) for line_index in
                  range(len(matrix))]
    print("after transposition  : ", transposed)
