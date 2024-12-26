from concurrent.futures import ThreadPoolExecutor

strings: list[str] = [
    "Да Здравствует ThreadPoolExecutor!!!",
    "Многопоточность в Python позволяет выполнять несколько задач одновременно, улучшая производительность.",
    "Многопоточность может увеличить сложность управления памятью и ресурсами.",
    "Правильное использование многопоточности в Python может значительно улучшить производительность приложений.",
]


def to_upper(string: str) -> None:
    return string.upper()


with ThreadPoolExecutor(max_workers=4) as executor:
    for string in strings:
        print(executor.submit(to_upper, string=string).result())
