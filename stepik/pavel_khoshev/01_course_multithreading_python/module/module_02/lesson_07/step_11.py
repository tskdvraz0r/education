import threading as t
from time import sleep
from concurrent.futures import ThreadPoolExecutor


unique_task_id: list[str] = [
    "StarExplorer42",
    "QuantumLeap89",
    "CyberWizard77",
    "GalacticVoyager66",
    "MysticCoder11",
    "NeuralNinja53",
    "QuantumRanger88",
    "SpaceSurfer15",
    "TimeTraveler23",
    "CosmicSage99",
]

result_lst: list = []


def thread_initializer() -> None:
    global result_lst
    thread_name: str = t.current_thread().name
    result_lst.append(f"Инициализация потока {thread_name}")


def thread_task(task_id: str) -> None:
    global result_lst
    thread_name: str = t.current_thread().name
    sleep(1)
    result_lst.append(f"Поток {thread_name} выполняет задачу {task_id}")


with ThreadPoolExecutor(
    max_workers=3,
    initializer=thread_initializer,
) as executor:
    [executor.submit(thread_task, task_id) for task_id in unique_task_id]

print(*result_lst, sep="\n")
      