import time
import threading as th


def task(sleep_time: int) -> None:
    print(f"Поток {th.current_thread().name} запустился.")
    time.sleep(sleep_time)


thread1: th.Thread = th.Thread(target=task, name="A", args=(2,))
thread2: th.Thread = th.Thread(target=task, name="B", args=(3,))

thread1.start()
thread2.start()

thread1.join(timeout=2.1)

for thread in (thread1, thread2):
    if thread.is_alive():
        print(f"Поток {thread.name} не завершился за установленное время.")
