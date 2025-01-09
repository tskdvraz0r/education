import sys
from collections.abc import Generator
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Lock, Thread
from time import sleep


sys.path.append("/Users/ts.kdv.raz0r/Yandex.Disk.localized/GitHub/education")
from packages.utils.decorators.time_spend import time_spend  # type: ignore

# Блокиратор "духовки";
oven_lock: Lock = Lock()

# Список имён поваров;
cooks_names: list[str] = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]

# Список видов пицц и время их приготовления;
pizzas: dict[str, int] = {
    "Маргарита": 3,
    "Пепперони": 2,
    "Вегетарианская": 4,
    "Четыре сыра": 5,
    "Гавайская": 3,
}


class Producer:
    def __init__(self, queue: Queue[tuple[str, str, int]]) -> None:
        self.queue: Queue[tuple[str, str, int]] = queue

    def get_data(self) -> Generator[tuple[str, str, int]]:
        for cook_name, pizza_name, delay in zip(
            cooks_names, pizzas.keys(), pizzas.values()
        ):
            yield (cook_name, pizza_name, delay)

    def produce(self) -> None:
        for cook_name, pizza_name, delay in self.get_data():
            self.queue.put(item=(cook_name, pizza_name, delay))


class Consumer:
    def __init__(self, queue: Queue[tuple[str, str, int]]) -> None:
        self.queue: Queue[tuple[str, str, int]] = queue

    def consume(self) -> None:
        while not self.queue.empty():
            cook_name, pizza_name, delay = self.queue.get()
            with oven_lock:
                print(f'{cook_name} начал(а) готовить пиццу "{pizza_name}".')
                sleep(delay)
                print(f'{cook_name} закончил(а) готовить пиццу "{pizza_name}".')
            self.queue.task_done()


@time_spend
def main() -> None:
    queue: Queue[tuple[str, str, int]] = Queue()

    producer: Producer = Producer(queue=queue)
    thread_producer = Thread(target=producer.produce)
    thread_producer.start()
    thread_producer.join()

    consumer: Consumer = Consumer(queue=queue)

    with ThreadPoolExecutor() as executor:
        executor.submit(consumer.consume)
    queue.join()

    print("Все пиццы приготовлены!")


if __name__ == "__main__":
    main()
