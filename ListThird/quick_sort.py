from typing import List


def qsort(xs: List[int]) -> List[int]:
    """ piwot xs[0] """
    lt_x = [lower for lower in xs[1:] if lower < xs[0]]
    gt_x = [greater for greater in xs[1:] if greater >= xs[0]]
    return qsort(lt_x) + [xs[0]] + qsort(gt_x) if xs else []


if __name__ == '__main__':
    test_list = [1, 6, 9, 2, 4, 7, 333, 41, 24, 35, 57, 4, 2, 5, 0, 1, 11]
    print(qsort(test_list))
