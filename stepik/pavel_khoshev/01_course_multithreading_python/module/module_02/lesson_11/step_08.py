import math
from typing import Callable, Any
from concurrent.futures import ThreadPoolExecutor, Future


small_numbers = list(range(1, 51))
medium_numbers = list(range(51, 151))
large_numbers = list(range(151, 301))


def square(number: int) -> int:
    return number**2


def cube(number: int) -> int:
    return number**3


def factorial(number: int) -> int:
    return math.factorial(number)


def process_number(number: int, func: Callable) -> dict[int, Any]:
    return {number: func(number)}


with ThreadPoolExecutor(max_workers=10) as executor:
    futures_small: list[Future[dict[int, Any]]] = [
        executor.submit(process_number, small_number, square)
        for small_number in small_numbers
    ]

    print("Результаты для маленьких чисел (возведение в квадрат):")
    for result in futures_small:
        print(result.result())

with ThreadPoolExecutor(max_workers=20) as executor:
    futures_meduim: list[Future[dict[int, Any]]] = [
        executor.submit(process_number, medium_number, cube)
        for medium_number in medium_numbers
    ]

    print("\nРезультаты для средних чисел (возведение в куб):")
    for result in futures_meduim:
        print(result.result())


with ThreadPoolExecutor(max_workers=30) as executor:
    futures_large: list[Future[dict[int, Any]]] = [
        executor.submit(process_number, large_number, factorial)
        for large_number in large_numbers
    ]

    print("\nРезультаты для больших чисел (факториал):")
    for result in futures_large:
        print(result.result())
