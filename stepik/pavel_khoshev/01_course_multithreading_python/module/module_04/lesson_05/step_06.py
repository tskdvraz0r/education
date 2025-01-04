import threading as t
import time
import queue

electronics = [
    "смартфон",
    "ноутбук",
    "планшет",
    "камера",
    "гарнитура",
    "телевизор",
    "гаджет",
    "монитор",
    "роутер",
    "плеер"
]

lock = t.Lock()

def producer(queue_: queue.Queue) -> None:
    for item in electronics:
        if queue_.empty():
            queue_.put(item)
            with lock:
                print(f"Поставлен товар: {item}")
        elif queue_.full():
            time.sleep(0.5)
            with lock:
                print("Склад временно заполнен")
        else:
            time.sleep(0.5)
            queue_.put(item)
            with lock:
                print(f"Поставлен товар: {item}")
    print("Поставки закончились")

def consumer(queue_: queue.Queue) -> None:
    while True:
        try:
            time.sleep(1)
            item = queue_.get()
        except queue.Empty:
            with lock:
                print("Склад временно пуст")
            continue
        else:
            with lock:
                print(f"Продан товар: {item}")
            queue_.task_done()

def main() -> None:
    queue_: queue.Queue = queue.Queue(maxsize=5)

    thread_producer = t.Thread(target=producer, args=(queue_,), daemon=True)
    thread_consumer = t.Thread(target=consumer, args=(queue_,), daemon=True)

    thread_consumer.start()
    thread_producer.start()

    thread_producer.join()
    queue_.join()

if __name__ == "__main__":
    main()