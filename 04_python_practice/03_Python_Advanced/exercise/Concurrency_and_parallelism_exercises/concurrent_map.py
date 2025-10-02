from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def add_one(x):
    return x + 1


def square(x):
    return x * x


def concurrent_map(fn, xs, backend="thread", max_workers=None):
    if backend == "thread":
        Executor = ThreadPoolExecutor
    elif backend == "process":
        Executor = ProcessPoolExecutor
    else:
        raise ValueError("backend must be 'thread' or 'process'")

    with Executor(max_workers=max_workers) as executor:
        futures = [executor.submit(fn, x) for x in xs]
        return [f.result() for f in futures]


if __name__ == "__main__":
    print(concurrent_map(add_one, [0, 1, 2], backend="thread"))  # [1,2,3]
    print(concurrent_map(square, [2, 3, 4], backend="process"))  # [4,9,16]
