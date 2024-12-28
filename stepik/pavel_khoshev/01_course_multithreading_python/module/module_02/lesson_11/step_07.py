from threading import Lock
from concurrent.futures import ThreadPoolExecutor

fifty: list[str] = ["OF95RK", "VH61DX", "NB03WA", "OL41DZ"]
one_hundred: list[str] = ["JF39XW", "RO06QB", "RW48XW", "ZE42EF"]
two_hundred: list[str] = ["FP99WI", "IJ21HS", "SV16JN", "EP11JG"]

stdout_lock = Lock()

def process_element(elem, pool_size) -> None:
    with stdout_lock:
        print(f"Элемент {elem} списка из пула размером {pool_size}")


def process_with_threadpool(elements, pool_size) -> None:
    with ThreadPoolExecutor(max_workers=pool_size) as executor:
        for elem in elements:
            executor.submit(process_element, elem, pool_size)


process_with_threadpool(fifty, 50)
process_with_threadpool(one_hundred, 100)
process_with_threadpool(two_hundred, 200)
