import math
import random
import sys
from typing import List, Generator


def generate_random_tree(tree_height: int) -> List:
    if tree_height < 0:
        raise ValueError('tree_height should be a positive number')
    upper_limit: int = int(math.pow(2, tree_height))
    lower_limit: int = int(math.pow(2, tree_height - 1) + 1)
    leaves_number: int = random.randint(lower_limit, upper_limit)
    root: List = ['1', None, None]
    if leaves_number < 2:
        return root
    generate_tree_nodes(root, 1, leaves_number)
    return root


def generate_tree_nodes(tree: List, previous_node: int, nodes_limit: int) -> List:
    left_node: int = 2 * previous_node
    right_node: int = 2 * previous_node + 1
    if previous_node > nodes_limit:
        return tree
    if left_node <= nodes_limit:
        tree[1] = [str(left_node), None, None]
    if right_node <= nodes_limit:
        tree[2] = [str(right_node), None, None]
    generate_tree_nodes(tree[1], left_node, nodes_limit)
    generate_tree_nodes(tree[2], right_node, nodes_limit)


def bfs_traveling(tree: List) -> Generator:
    flatten_function = lambda nodes: [item for sublist in filter(None, nodes) for item in sublist]
    to_visit: List = tree.copy()
    tmp: List = tree.copy()
    while len(to_visit) > 0:
        for i in range(0, len(to_visit)):
            if not isinstance(to_visit[i], List):
                yield to_visit[i]
        for i in range(len(to_visit) - 1, -1, -1):
            if isinstance(to_visit[i], str):
                tmp.pop(i)

        to_visit = flatten_function(tmp)
        tmp = to_visit.copy()


def dfs_traveling(tree: List) -> Generator:
    if tree is None:
        yield None
        return
    yield tree[0]
    yield from dfs_traveling(tree[1])
    yield from dfs_traveling(tree[2])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python tree.py tree_height")
        exit(1)

    tree = generate_random_tree(int(sys.argv[1]))
    print(tree)
    print(list(bfs_traveling(tree)))
    print(list(dfs_traveling(tree)))
