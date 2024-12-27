from math import factorial
from time import sleep
from concurrent.futures import Future, ThreadPoolExecutor, as_completed


numbers: list[str] = [3, 6, 14, 20, 5, 7, 2]


def calc_fact_or_square(number: int) -> tuple[int, int]:
    print(f"Обработка числа {number} началась")
    sleep(number / 10)
    return number, factorial(number) if number <= 7 else number**2


executor = ThreadPoolExecutor(max_workers=len(numbers))
futures: list[Future[tuple[int, int]]] = [
    executor.submit(calc_fact_or_square, number) for number in numbers
]
executor.shutdown(wait=False)

sleep(0.1)
try:
    executor.submit(calc_fact_or_square, 42)

except Exception:
    print("Пул потоков остановлен! Передача новых задач в него невозможна!")

for future_result in as_completed(futures):
    number, result = future_result.result()
    print(f"Результат обработки {number} = {result}")
