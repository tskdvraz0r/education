import threading as th

local_storage = th.local()


def process_data() -> None:
    local_storage.data = "HELLO LOCAL STORAGE!"
    print(f"Данные в локальном хранилище: {local_storage.data}")


for _ in range(3):
    th.Thread(target=process_data).start()
