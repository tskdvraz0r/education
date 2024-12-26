from concurrent.futures import ThreadPoolExecutor, Future


messages: list[str] = [
    "Привет, давайте обсудим многопоточность в Python!",
    "Да, GIL - это большая проблема для многопоточности в Python.",
]
result: list = []


def count_chars(string: str) -> int:
    return len(string)


with ThreadPoolExecutor() as executor:
    futures: list[Future[int]] = [
        executor.submit(count_chars, message) for message in messages
    ]
    for future in futures:
        result.append(future.result())

print(f"Общее количество символов в каждой строке: {result}")
