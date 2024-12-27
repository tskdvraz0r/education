import threading as t
from math import factorial
from time import sleep
from concurrent.futures import ThreadPoolExecutor


numbers: list[str] = [19, 1, 4, 13, 10, 7, 16]
result = 0


def calc_fact_or_square(number: int) -> int:
    global result
    print(f"Обработка числа {number} началась")
    sleep(number / 10)
    with t.Lock():
        result += factorial(number) if number <= 7 else number**2


executor = ThreadPoolExecutor()
executor.map(calc_fact_or_square, numbers)
executor.shutdown()
print(f"Сумма обработанных чисел равна {result}")
