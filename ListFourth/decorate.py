import time


def time_measure(fn):
    fn.work_time = time.time_ns()

    def modified_fn(*args):
        fn1 = fn(*args)
        print(fn.__name__, "work time:", ((time.time_ns() - fn.work_time) / 1_000_000), "ms")
        return fn1

    return modified_fn


@time_measure
def test(a, b, c):
    time.sleep(1)
    return (a * b * c) ** c


if __name__ == '__main__':
    print(test(1, 1, 1))
