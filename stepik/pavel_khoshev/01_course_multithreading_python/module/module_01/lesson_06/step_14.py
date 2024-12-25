import time
import threading as th


def print_from_one_to_five() -> None:
    for i in range(1, 6):
        time.sleep(0.5)
        print(i)


def print_from_a_to_e() -> None:
    for i in "abcde":
        time.sleep(1)
        print(i)


thread1: th.Thread = th.Thread(target=print_from_one_to_five)
thread2: th.Thread = th.Thread(target=print_from_a_to_e)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Готово!")
