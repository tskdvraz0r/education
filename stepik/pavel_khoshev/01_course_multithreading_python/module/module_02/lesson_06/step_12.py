from time import sleep
from math import prod
from concurrent.futures import ThreadPoolExecutor, wait

work_times = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]

numbers = [
    [2, 5],
    [6, 2],
    [9, 4],
    [2, 2],
    [2, 8],
    [3, 5],
    [4, 1],
    [6, 2],
    [7, 4],
    [9, 7],
    [5, 7],
    [3, 8],
    [4, 0],
    [8, 2],
    [6, 9],
    [9, 7],
    [3, 6],
    [6, 7],
    [2, 5],
    [7, 3],
]


def calc_sum_or_mult(delay: int, numbers: list[int, int]) -> int:
    sleep(delay)
    return prod(numbers) if (delay & 1) == 0 else sum(numbers)


with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(calc_sum_or_mult, time, values) for time, values in zip(work_times, numbers)]
    done, undone = wait(futures, timeout=2.5)

    for result in done:
        print(result.result())
