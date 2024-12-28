from concurrent.futures import ThreadPoolExecutor, Future
from math import prod

list1: list[int] = [16, 10, 11, 20]
list2: list[int] = [1, 0, 6, 4]
list3: list[int] = [8, 19, 14, 13]
list4: list[int] = [1, 0, 3, 6]


def mult_numbers(numbers: tuple[int, int, int, int]) -> int:
    if 0 in numbers:
        raise ValueError("Обнаружено умножение на ноль")
    return prod(numbers)


with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(mult_numbers, values)
        for values in zip(list1, list2, list3, list4)
    ]

    for future in futures:
        if future.exception() is None:
            print(f"Результат: {future.result()}")
        else:
            print(f"Обработано исключение: {future.exception()}")
