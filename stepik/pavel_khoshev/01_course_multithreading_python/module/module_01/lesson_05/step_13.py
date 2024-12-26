import time
import threading as th


def print_from_one_to_five() -> None:
    for i in range(1, 6):
        time.sleep(0.5)
        print(i)


def print_from_six_to_ten() -> None:
    for i in range(6, 11):
        time.sleep(1)
        print(i)


thread1: th.Thread = th.Thread(target=print_from_one_to_five)
thread2: th.Thread = th.Thread(target=print_from_six_to_ten)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Оба потока завершили свою работу.")
