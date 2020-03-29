import sys


def generate_random_tree(tree_height):
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python tree.py tree_size")
        exit(1)
    generate_random_tree(sys.argv[1])