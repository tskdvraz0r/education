import time
import threading as t
from queue import Queue, Empty



elements = [
    'телевизор',
    'холодильник',
    'микроволновка',
    'утюг',
    'чайник',
    'пылесос',
    'стиральная машина',
    'кофеварка',
    'фен',
    'утюг'
]

class Procedure:
    def __init__(self, queue: Queue):
        self.queue = queue

    def executor(self) -> None:
        for value in elements:
            self.queue.put(value)
            print(f"Добавлен: {value}")
            time.sleep(0.5)
        print("Все элементы добавлены")

class Consumer:
    def __init__(self, queue: Queue):
        self.queue = queue

    def executor(self) -> None:
        while True:
            time.sleep(1)
            try:
                value: str = self.queue.get()
            except Empty:
                continue
            else:
                print(f"Извлечен: {value}")
                self.queue.task_done()

def main():
    # Создание экземпляра очереди;
    queue: Queue = Queue()

    # Создание и запуск потока-производителя;
    procedure = Procedure(queue=queue)
    procedure_thread: t.Thread = t.Thread(target=procedure.executor, daemon=True)
    procedure_thread.start()

    # Создание и запуск потока-потребителя;
    consumer = Consumer(queue=queue)
    consumer_thread: t.Thread = t.Thread(target=consumer.executor, daemon=True)
    consumer_thread.start()

    # Ожидание завершения добавления всех элементов в очередь;
    procedure_thread.join()

    # Ожидание обработки всех элементов очереди;
    queue.join()

    print("Все элементы очереди обработаны")

if __name__ == "__main__":
    main()