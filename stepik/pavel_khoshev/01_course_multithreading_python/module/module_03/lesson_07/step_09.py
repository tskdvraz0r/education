import typing
import random
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, Future

data: typing.Iterable = range(1, 21)
thread_lock: Lock = Lock()

def process_data(item: int) -> int:
    if random.random() < 0.2:
        raise ValueError(f"Ошибка обработки элемента {item}")
    else:
        return item

def result(future: Future) -> None:
    if future.exception() is None:
        with thread_lock:
            print(f"Элемент {future.result()} обработан успешно.")
    else:
        number: str = str(future.exception()).split()[-1]
        with thread_lock:
            print(f"Элемент {number} вызвал ошибку: {future.exception()}")

with ThreadPoolExecutor() as executor:
    futures: list[Future] = [
        executor.submit(process_data, item)
        for item in data
    ]

    for future in futures:
        future.add_done_callback(result)