import time
import threading as th


file_names: list[str] = ["file623.xlsx", "file538.jpg", "file13.txt"]
results: list = []


def load_file(filename: str) -> None:
    global results

    results.append(f"{th.current_thread().name} начал загрузку файла {filename}.")
    time.sleep(1)
    results.append(f"{th.current_thread().name} завершил загрузку файла {filename}.")


def process_file(filename: str) -> None:
    global results

    results.append(f"{th.current_thread().name} начал обработку файла {filename}.")
    time.sleep(1)
    results.append(f"{th.current_thread().name} завершил обработку файла {filename}.")


def save_file(filename: str) -> None:
    global results

    results.append(f"{th.current_thread().name} начал сохранение файла {filename}.")
    time.sleep(1)
    results.append(f"{th.current_thread().name} завершил сохранение файла {filename}.")


def main(filename: str) -> None:
    thread1: th.Thread = th.Thread(
        target=load_file, name=f"LoadThread-{filename}", kwargs={"filename": filename}
    )
    thread2: th.Thread = th.Thread(
        target=process_file,
        name=f"ProcessThread-{filename}",
        kwargs={"filename": filename},
    )
    thread3: th.Thread = th.Thread(
        target=save_file, name=f"SaveThread-{filename}", kwargs={"filename": filename}
    )

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


for filename in file_names:
    main(filename=filename)

for result in results:
    print(result)
