from time import sleep
from concurrent.futures import ThreadPoolExecutor, Future


data = {
    1.4: 'ljeo',
    0.4: 'akwx',
    2.3: 'tydx',
    2.7: 'qnai',
    2.6: 'smgx',
    1.9: 'fhef',
    1.6: 'wzag',
    2.5: 'hjsz',
    2.4: 'gpay',
    0.5: 'wxco'
}


def task(data) -> None:
    delay, task_name = data
    sleep(delay)
    print(f"Задача {task_name} выполнилась.")


with ThreadPoolExecutor(max_workers=2) as executor:
    for elem in data.items():
        future = executor.submit(task, elem)
        if int(str(elem[0]).split(".")[-1]) % 2 != 0:
            future.cancel()