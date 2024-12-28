from threading import Lock
from time import sleep
from concurrent.futures import ThreadPoolExecutor, Future

inventory = {
    "Intel Core i9": 120, 
    "Intel Core i7": 66, 
    "Intel Core i5": 60, 
    "Intel Core i3": 1, 
    "Intel Xeon": 81,
    "AMD Ryzen 9": 56, 
    "AMD Ryzen 7": 55, 
    "AMD Ryzen 5": 0, 
    "AMD Ryzen 3": 1, 
    "AMD Threadripper": 41, 
    "AMD Epyc": 3,
    "Intel Pentium": 19, 
    "Intel Celeron": 2, 
    "Qualcomm Snapdragon 888": 54, 
    "Apple M1": 14, 
    "Apple A14 Bionic": 20,
    "ARM Cortex-A78": 0, 
    "ARM Cortex-A55": 87, 
    "ARM Cortex-M4": 30, 
    "NVIDIA Tegra X1": 2,
    "Samsung Exynos 2100": 22,
    "MediaTek Dimensity 1000": 0, 
    "Intel Atom": 0, "AMD Athlon": 95, 
    "AMD Sempron": 30, 
    "Intel Core 2 Duo": 2,
    "Intel Core 2 Quad": 1, 
    "Intel Itanium": 2, 
    "AMD Duron": 98, "AMD FX": 0
}

stdout_lock = Lock()


def search_product(product_id: str) -> str:
    id: str = product_id
    with stdout_lock:
        print(f"Поиск товара {id}. Количество на складе: {inventory[id]} шт")
    return id

def process_order(future: Future) -> None:
    global inventory

    id: str = future.result()
    if inventory[id] > 0:
        with stdout_lock:
            inventory[id] -= 1
            print(
                f"Товар отправлен получателю {id}. Количество на складе: {inventory[id]} шт"
            )
    else:
        with stdout_lock:
            print(f"Товара {id} нет в наличии, обработка невозможна.")


with ThreadPoolExecutor() as executor:
    futures: list[Future] = [
        executor.submit(search_product, product_id)
        for product_id in inventory.keys()
    ]

    for future in futures:
        future.add_done_callback(process_order)