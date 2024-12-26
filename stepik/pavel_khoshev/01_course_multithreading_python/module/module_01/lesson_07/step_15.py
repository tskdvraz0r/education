import time
import threading as th

thread_names: list[str] = [
    "OF95RK",
    "VH61DX",
    "NB03WA",
    "WO40ZF",
    "NJ48EG",
    "SX21ET",
    "AT01PA",
    "MR36DD",
    "DD84HR",
    "MI81QY",
]


def worker() -> None:
    print(f"{th.current_thread().name} начал работу.")
    time.sleep(1)
    print(f"{th.current_thread().name} завершил работу.")


for thread_name in thread_names:
    th.Thread(target=worker, name=f"Name_thread-{thread_name}").start()
