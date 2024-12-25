import threading as th
import numpy as np

numbers: np.ndarray = np.array([123456, 7890123, 987654, 114455, 995423, 1000000])
total_sum: int = 0

def sum_numbers() -> None:
    global total_sum
    total_sum = np.sum(numbers)

def thread_task() -> None:
    sum_numbers()

thread: th.Thread = th.Thread(target=thread_task)
thread.start()
thread.join()

print(total_sum)
