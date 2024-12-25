import time
import random as rd
import threading as th


missions: dict[str, str] = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",
}


def mission(mission_name: str) -> None:
    print(f"[{mission_name}] Миссия началась.")
    time.sleep(rd.randint(1, 3))
    print(f"[{mission_name}] Миссия успешно выполнена!")


for thread_name, mission_name in missions.items():
    thread: th.Thread = th.Thread(target=mission, args=(mission_name,), name=thread_name)
    print(f"[{thread_name} ({mission_name})] Статус миссии до запуска: {thread.is_alive()}")
    thread.start()
    print(f"[{thread_name} ({mission_name})] Миссия активна: {thread.is_alive()}")
    thread.join()
    print(f"[{thread.name} ({mission_name})] Статус миссии после завершения: {not thread.is_alive()}")