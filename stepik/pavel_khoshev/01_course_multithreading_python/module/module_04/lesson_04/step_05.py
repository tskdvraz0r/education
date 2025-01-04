import threading as t
import time
from queue import PriorityQueue, Empty



electronics = [
    (1, "смартфон"),
    (15, "ноутбук"),
    (7, "планшет"),
    (33, "камера"),
    (67, "гарнитура"),
    (4, "телевизор"),
    (21, "гаджет"),
    (83, "монитор"),
    (0, "роутер"),
    (47, "плеер")
]
lock = t.Lock()

def producer(p_queue: PriorityQueue) -> None:
    for element in electronics:
        p_queue.put(element)

def comsumer(p_queue: PriorityQueue) -> None:
    while True:
        try:
            item = p_queue.get()
            time.sleep(item[0] / 100)
        except Empty:
            continue
        else:
            with lock:
                print(f'Обработан: "{item[1]}"')
            p_queue.task_done()

def main() -> None:
    # Экземпляр приоритетной очереди, размерностью 5;
    p_queue: PriorityQueue = PriorityQueue(maxsize=5)

    # Создание и запуск потока-производителя;
    thread_producer = t.Thread(target=producer, args=(p_queue,), daemon=True)
    thread_producer.start()

    # Создание и запуск потока-потребителя;
    threads_consumer = [
        t.Thread(target=comsumer, args=(p_queue,), daemon=True)
        for _ in range(2)

    ]
    for thread_consumer in threads_consumer:
        thread_consumer.start()

    thread_producer.join()
    p_queue.join()

if __name__ == "__main__":
    main()