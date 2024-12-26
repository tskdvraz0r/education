import time
import threading as th

astronauts: list[str] = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks: list[str] = [
    "Ремонт оборудования",
    "Проведение экспериментов",
    "Мониторинг систем",
]
intervals: list[float] = [0.7, 1.3, 1.8]


def worker(interval: float, astronaut: str, task: str) -> None:
    time.sleep(interval)
    print(f"{astronaut} выполняет задачу: {task}")


for interval, astronaut, task in zip(intervals, astronauts, tasks):
    th.Thread(target=worker, args=(interval, astronaut, task)).start()
