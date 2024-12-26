import math
from concurrent.futures import Future, ThreadPoolExecutor


def fib_future() -> None:
    number: int = 20
    result: int = int(
        (((1 + math.sqrt(5)) / 2) ** number - ((1 - math.sqrt(5)) / 2) ** number)
        / math.sqrt(5)
    )
    print(f"20-е число Фибоначчи: {result}")


def sqrt_future() -> None:
    result = sum([math.sqrt(i) for i in range(1, 51)])
    print(f"Сумма квадратных корней чисел от 1 до 50: {result:.4f}")


def fact_future() -> None:
    print(f"Факториал числа 20: {math.factorial(20)}")


with ThreadPoolExecutor() as executor:
    for func in (fib_future, sqrt_future, fact_future):
        future: Future = executor.submit(func)
        future.result()
