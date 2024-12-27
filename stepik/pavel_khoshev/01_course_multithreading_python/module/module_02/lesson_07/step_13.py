import threading as t
from time import sleep
from concurrent.futures import ThreadPoolExecutor


global_storage: dict = {}
local_storage = t.local()
numbers: list[int] = [
    6359, 5217, 5411, 3615, 1524, 5946, 5693, 9662, 8922, 1657, 6202, 2930,
    2651, 6594, 4482, 5504, 6084, 5142, 3272, 1934, 1002, 7333, 2003, 9584,
    1018, 1882, 5929, 3411, 8984, 8886, 7037, 4988, 6961, 2602, 8114, 4462,
    3908, 3549, 3812, 5882, 7907, 2438, 2210, 3879, 3765, 8623, 1654, 3562,
    5205, 5082, 8443, 8742, 9058, 6979, 7968, 2205, 8830, 8798, 2028, 7474,
    8519, 1853, 1815, 3194, 3700, 9318, 2716, 5772, 8939, 8925, 1594, 9005,
    5326, 4190, 8645, 6392, 6583, 8614, 5242, 2417, 7037, 2122, 8311, 6808,
    9534, 7189, 1493, 8339, 1669, 2605, 1653, 3423, 6555, 6779, 1749, 3709,
    4545, 8217, 5080, 8658, 2731, 7139, 6508, 2515, 2280, 7627, 3565, 9623,
    7520, 5807, 5403, 1356, 7310, 3268, 3320, 4320, 6361, 4625, 7427, 2781,
]


def setup_environment() -> None:
    local_storage.counter = 0


def process_task(number: int) -> None:
    global global_storage
    
    sleep(0.1)
    local_storage.counter += 1
    if t.current_thread().name not in global_storage:
        global_storage[t.current_thread().name] = 0
    global_storage[t.current_thread().name] += 1
        

with ThreadPoolExecutor(
    max_workers=10, initializer=setup_environment, thread_name_prefix="environment"
) as executor:
    executor.map(process_task, [i for i in numbers if (i & 1) == 0])

for key, value in global_storage.items():
    print(f"{key} - Чисел обработано: {value}")
