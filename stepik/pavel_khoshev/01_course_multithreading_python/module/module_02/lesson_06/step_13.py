from math import factorial
from time import sleep
from concurrent.futures import ThreadPoolExecutor


numbers: list[int] = [5, 4, 7, 6, 3]


def calc_factorial(number: int) -> int:
    sleep(number / 10)
    return f"Факториал числа {number} равен {factorial(number)}"


with ThreadPoolExecutor() as executor:
    results = executor.map(calc_factorial, numbers)

    for result in results:
        print(result)
