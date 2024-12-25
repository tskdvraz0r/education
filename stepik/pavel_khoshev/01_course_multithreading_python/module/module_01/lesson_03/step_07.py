import threading as th
import numpy as np


total_sum: int = 0
total_mult: int = 0


def sum_numbers() -> None:
    global total_sum
    total_sum = np.sum(np.arange(1, 1001))

def mult_numbers() -> None:
    global total_mult
    total_mult = np.prod(np.arange(1, 11))

thread1: th.Thread = th.Thread(target=sum_numbers)
thread2: th.Thread = th.Thread(target=mult_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Сумма чисел от 1 до 1000: {total_sum}")
print(f"Произведение чисел от 1 до 10: {total_mult}")
