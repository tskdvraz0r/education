import time
import threading as th


code_names: list = [
    "Alpha",
    "Bravo",
    "Delta",
    "Charley",
    "Echo"
]


def task(code_name: str) -> None:
    thread: th.Thread = th.current_thread()
    print(f"Исходное имя потока: {thread.name}")
    thread.name = code_name
    print(f"Новое имя потока: {thread.name}")
    time.sleep(1)
    print(f"Задача выполнена для {th.current_thread().name}")


for code_name in code_names:
    th.Thread(target=task, args=(code_name,)).start()