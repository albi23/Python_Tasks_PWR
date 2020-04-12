import math
import random
import sys
from typing import List, Generator


def generate_random_tree(tree_height: int) -> List:
    if tree_height < 0:
        raise ValueError('tree_height should be a positive')
    upper_limit: int = int(math.pow(2, tree_height))
    lower_limit: int = int(math.pow(2, tree_height - 1) + 1)
    leaves_number: int = random.randint(lower_limit, upper_limit)
    root = ['1', None, None]
    if leaves_number < 2:
        return root
    generate_tree_nodes(root, 1, leaves_number)
    return root


def generate_tree_nodes(root: List, previous_child: int, nodes_limit: int) -> List:
    left_node = 2 * previous_child
    right_node = 2 * previous_child + 1
    if previous_child > nodes_limit:
        return root
    if left_node <= nodes_limit:
        root[1] = [str(left_node), None, None]
    if right_node <= nodes_limit:
        root[2] = [str(right_node), None, None]
    generate_tree_nodes(root[1], left_node, nodes_limit)
    generate_tree_nodes(root[2], right_node, nodes_limit)


def bfs_traveling(tree: List) -> Generator:
    flatten = lambda nodes: [item for sublist in filter(None, nodes) for item in sublist]
    to_visit: List = tree.copy()
    tmp: List = tree.copy()
    while len(to_visit) > 0:
        for i in range(0, len(to_visit)):
            if not isinstance(to_visit[i], List):
                yield to_visit[i]
        for i in range(len(to_visit) - 1, -1, -1):
            if isinstance(to_visit[i], str):
                tmp.pop(i)

        to_visit = flatten(tmp)
        tmp = to_visit.copy()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python tree.py tree_size")
        exit(1)

    tree = generate_random_tree(int(sys.argv[1]))
    print(tree)
    print(list(bfs_traveling(tree)))


    # flat_list = []
    # for sublist in l:
    #     for item in sublist:
    #         flat_list.append(item)
    # a = ['1',
    #      ['2',
    #       ['4',
    #        ['8', None, None],
    #        ['9', None, None]
    #        ],
    #       ['5',
    #        ['10', None, None], None]
    #       ],
    #      ['3',
    #       ['6', None, None],
    #       ['7', None, None]
    #       ]
    #      ]

#                    1
#       2                      3
#    4         5             6    7
# 8    9     10
