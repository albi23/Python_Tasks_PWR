from typing import List, Generator


def flatten(data: List) -> Generator:
    for elem in data:
        if isinstance(elem, List):
            yield from flatten(elem)
        else:
            yield elem


if __name__ == '__main__':
    data_list = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]
    print(list(flatten(data_list)))
