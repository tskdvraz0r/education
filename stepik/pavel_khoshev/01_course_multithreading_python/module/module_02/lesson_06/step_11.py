from time import sleep
from concurrent.futures import ThreadPoolExecutor, Future, wait


data = [
    ("asdf", 0.7),
    ("ghjk", 1.4),
    ("zxcl", 3.2),
    ("vbnm", 4.1),
    ("poiu", 2.7),
    ("ytre", 0.3),
    ("wqsx", 1.1),
]


def task(data: tuple[str, int]) -> None:
    name, time = data
    sleep(time)
    return name


with ThreadPoolExecutor() as executor:
    futures: list[Future] = [executor.submit(task, values) for values in data]
    done, not_done = wait(fs=futures, timeout=1.5)

    for future in done:
        print(future.result())
