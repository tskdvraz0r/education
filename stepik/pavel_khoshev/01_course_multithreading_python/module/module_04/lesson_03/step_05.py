import threading as t
from queue import LifoQueue, Empty

data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]

def producer(stack: LifoQueue) -> None:
    for i in data:
        stack.put(i)

def consumer(stack: LifoQueue) -> None:
    while True:
        try:
            item: int = stack.get()
        except Empty:
            print("Очередь пуста;")
            continue
        else:
            print(f"Обработка элемента: {item}")
            stack.task_done()

def main():
    stack: LifoQueue = LifoQueue()

    thread_producer: t.Thread = t.Thread(target=producer, args=(stack,), daemon=True)
    thread_producer.start()
    thread_producer.join()

    threads = [t.Thread(target=consumer, args=(stack,), daemon=True) for _ in range(3)]
    for thread in threads:
        thread.start()

    stack.join()

    print("Все элементы успешно обработаны")

if __name__ == "__main__":
    main()