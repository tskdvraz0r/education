import threading as th
import numpy as np

numbers: np.ndarray = np.array(
    [
        456, 467, 961, 561, 512,
        740, 6412, 464, 444, 102,
        456, 347, 905, 854, 901,
        326, 267, 236, 790, 235,
        745,769, 467, 734, 745,
        895, 445, 312, 123, 451,
        523, 567, 344, 234
    ]
)
sum_even: int = 0
sum_odd: int = 0


def sum_even_numbers() -> None:
    global sum_even
    sum_even = np.sum(numbers[np.where((numbers & 1) == 0)])


def sum_odd_numbers() -> None:
    global sum_odd
    sum_odd = np.sum(numbers[np.where((numbers & 1) != 0)])


thread_even: th.Thread = th.Thread(target=sum_even_numbers)
thread_odd: th.Thread = th.Thread(target=sum_odd_numbers)

thread_even.start()
thread_odd.start()

thread_even.join()
thread_odd.join()

print(f"Сумма четных чисел: {sum_even}")
print(f"Сумма нечетных чисел: {sum_odd}")
