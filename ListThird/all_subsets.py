def get_all_subsets(list_data):
    return get_all_subsets(list_data[1:]) + [item + [list_data[0]] for item in
                                             get_all_subsets(list_data[1:])] if list_data else [[]]


if __name__ == '__main__':
    tests_list = [1, 2, 3, 4, 5]
    print((get_all_subsets(tests_list)))
