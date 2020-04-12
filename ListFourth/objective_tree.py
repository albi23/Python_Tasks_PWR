import math
import random
import sys
from typing import Generator, List


class Node:

    def __init__(self, parent, value: str):
        self.parent = parent
        self.value: str = value
        self.nodes: List[Node] = list()

    def add_node(self, node):
        self.nodes += node


def gen_random_tree(tree_height: int) -> Node:
    if tree_height < 0:
        raise ValueError('tree_height should be a positive number')
    child_nodes = int(random.randint(2, max(3, tree_height)))
    upper_limit: int = int(math.pow(child_nodes, tree_height))
    lower_limit: int = int(math.pow(child_nodes, tree_height - 1) + 1)
    all_leaves_limit: int = random.randint(lower_limit, upper_limit)

    root = Node(None, "1")
    if tree_height == 1:
        return root

    nodes_to_fill: List = [root]
    counter: int = 1
    while True:
        current_root = nodes_to_fill.pop(0)
        new_child_number = random.randint(2, child_nodes)
        if counter + new_child_number > all_leaves_limit:
            if all_leaves_limit - counter <= 0:
                return root
            else:
                new_child_number = all_leaves_limit - counter

        for i in range(1, new_child_number + 1):
            counter += 1
            new_node = Node(current_root, str(counter))
            nodes_to_fill.extend({new_node})
            current_root.add_node({new_node})


def bfs_traveling(tree: Node) -> Generator:
    travel: List = [tree]
    while len(travel) > 0:
        current_root = travel.pop(0)
        yield current_root.value
        for child in current_root.nodes:
            travel.extend({child})


def dfs_traveling(tree: Node) -> Generator:
    stack: List = [tree]
    visited = {}
    while len(stack) > 0:
        node = stack.pop(0)
        if visited.get(node.value) is None:
            visited[node.value] = True
            yield node.value

        for child in node.nodes:
            if visited.get(child.value) in [None, False]:
                stack.insert(0, child)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python objective_tree.py tree_height")
        exit(1)

    root_tree = gen_random_tree(int(sys.argv[1]))
    print(list(bfs_traveling(root_tree)))
    print(list(dfs_traveling(root_tree)))
