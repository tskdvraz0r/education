from time import sleep
from concurrent.futures import ThreadPoolExecutor, Future

data = [
    ('CPU', 3.1),
    ('RAM', 1.5),
    ('GPU', 1.6),
    ('Motherboard', 1.8),
    ('SSD', 1.3),
    ('Keyboard', 1.5),
    ('Mouse', 3.9),
    ('Monitor', 2.8),
    ('Headphones', 3.0),
    ('Router', 1.0)
]

def task(values: tuple[str, float]) -> None:
    task_name, delay = values
    sleep(delay)
    print(f"Задача {task_name} выполнилась за {delay} секунды")

with ThreadPoolExecutor(max_workers=5) as executor:
    futures: list[Future] = [
        executor.submit(task, values)
        for values in data
    ]

    for future in futures[5:]:
        future.cancel()