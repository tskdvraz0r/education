import time
import threading as th


delays: list[float] = [0.7, 2.4, 1, 8, 4.3, 0.4, 1.3, 2.5, 1.7, 3.2, 4.7, 3.6]


def my_task(time_for_work: int) -> None:
    print(f"Поток {th.current_thread().name} начал работу")
    time.sleep(time_for_work)
    print(f"Поток {th.current_thread().name} завершил работу")


for delay in delays:
    th.Thread(target=my_task, args=(delay,)).start()


time.sleep(1.5)
for thread_name in th.enumerate():
    print(f"{thread_name.name} еще выполняется")
