import threading as t
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from typing import Generator, Any


def get_unique_thread_id() -> Generator[str, Any, None]:
    unique_thread_ids: list[str] = [
        "KFD34",
        "DGS6D",
        "F7F9S",
        "SDG0D",
        "WQ9WE",
        "29AXC",
        "AF632",
        "DCV13",
        "Q9ETF",
        "1D0S3",
    ]

    for thread_id in unique_thread_ids:
        yield thread_id


unique_thread_id = get_unique_thread_id()


def thread_initializer() -> None:
    thread_id: str = next(unique_thread_id)
    with t.Lock():
        print(f"Инициализация потока: {thread_id}")


def thread_task(num: int) -> None:
    with t.Lock():
        print(f"Задача {num} запущена")
    sleep(0.1)
    with t.Lock():
        print(f"Задача {num} выполнена")


with ThreadPoolExecutor(max_workers=10, initializer=thread_initializer) as executor:
    executor.map(thread_task, range(10))
