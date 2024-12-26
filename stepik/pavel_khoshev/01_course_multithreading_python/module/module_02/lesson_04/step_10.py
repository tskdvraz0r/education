from time import sleep
from concurrent.futures import ThreadPoolExecutor


data = [
    ("asdf", 0.7),
    ("ghjk", 1.4),
    ("zxcl", 3.2),
    ("vbnm", 4.1),
    ("poiu", 2.7),
    ("ytre", 0.3),
    ("wqsx", 1.1),
]


def task(
    name: str,
    sleep_time: int,
) -> None:
    sleep(sleep_time)
    return name


with ThreadPoolExecutor() as executor:
    futures = [executor.submit(task, *values) for values in data]
    
    for future in futures:
        try:
            result = future.result(timeout=1.5)
            print(result)

        except TimeoutError:
            print("wait")
