from concurrent.futures import ThreadPoolExecutor, Future
from threading import Lock


devices = [
    {"name": "Server1", "ip": "192.168.1.1", 'status': True},
    {"name": "Router1", "ip": "192.168.1.2", 'status': True},
    {"name": "Switch1", "ip": "192.168.1.3", 'status': False},
    {"name": "Server10", "ip": "192.168.1.28", 'status': True},
    {"name": "Router10", "ip": "192.168.1.29", 'status': False},
    {"name": "Switch10", "ip": "192.168.1.30", 'status': True}
]

thread_lock: Lock = Lock()


def monitor_device(device: dict) -> dict:
    with thread_lock:
        print(f"Мониторинг устройства: {device['name']}, с IP {device['ip']} статус: "
              f"{device['status']}")
    return device


def handle_device_status(future: Future) -> None:
    device: dict = future.result()
    if device["status"]:
        with thread_lock:
            print(f"Устройство {device['name']} активно и работает нормально.")
    else:
        print(f"Внимание: Устройство {device['name']} неактивно! Включаем устройство.")
        device["status"] = True
        print(f"Устройство {device['name']} успешно включено!")


with ThreadPoolExecutor() as executor:
    futures: list[Future] = [
        executor.submit(monitor_device, device)
        for device in devices
    ]

    for future in futures:
        future.add_done_callback(handle_device_status)
