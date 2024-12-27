from string import punctuation
from collections import Counter
from concurrent.futures import ThreadPoolExecutor


messages: list[str] = [
    "Привет, коллеги! Кто-нибудь может объяснить разницу между асинхронным и многопоточным программированием в Python?",
    "Асинхронное программирование позволяет обрабатывать несколько задач без блокировки основного потока.",
    "Многопоточное программирование также обеспечивает параллельное выполнение, но с использованием потоков вместо асинхронных задач.",
    "Помните, что асинхронное программирование может требовать пересмотра структуры кода и логики приложения.",
    "Многопроцессорное программирование может использовать модуль multiprocessing.Event для организации событийного взаимодействия между процессами.",
    "Асинхронные функции могут использовать asyncio.ensure_future() для запуска задачи в асинхронном режиме.",
]

COUNTER = Counter()


def count_letters(text: str):
    for char in punctuation + " 01234567890":
        text = text.lower().replace(char, "")
    return Counter(text.lower())


with ThreadPoolExecutor() as executor:
    futures = [executor.submit(count_letters, message) for message in messages]
    for future in futures:
        COUNTER.update(future.result())

print(dict(sorted(COUNTER.items())))
