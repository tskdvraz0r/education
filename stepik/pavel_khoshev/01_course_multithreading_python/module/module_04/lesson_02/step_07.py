import os
from threading import Thread
from queue import Queue, Empty


PATH_DATA: str = "/Users/ts.kdv.raz0r/Yandex.Disk.localized/GitHub/education/stepik/pavel_khoshev/01_course_multithreading_python/module/module_04/lesson_02/data"

class DataExtractor:
    def __init__(self, queue_files: Queue) -> None:
        self._queue_files: Queue[list[str]] = queue_files

    @property
    def queue_files(self) -> Queue[list[str]]:
        return self._queue_files

    def from_txt(self, filepath: str) -> None:
        with open(file=filepath, mode="r", encoding="UTF-8") as file:
            self.queue_files.put(file.readlines())


class DataProducer:
    def __init__(self, queue_files: Queue) -> None:
        self._queue_files: Queue[list[str]] = queue_files

    @property
    def queue_files(self) -> Queue[list[str]]:
        return self._queue_files

    def put_data_in_queue(self):
        for filename in os.listdir(PATH_DATA):
            DataExtractor(queue_files=self.queue_files).from_txt(filepath=f"{PATH_DATA}/{filename}")


class DataTransform:
    def __init__(self) -> None:
        self._total_rows: int = 0
        self._total_words: int = 0

    @property
    def total_rows(self) -> int:
        return self._total_rows

    @property
    def total_words(self) -> int:
        return self._total_words

    @total_rows.setter
    def total_rows(self, value: int) -> None:
        self._total_rows = value

    @total_words.setter
    def total_words(self, value: int) -> None:
        self._total_words = value

    def add_rows(self, value: int) -> None:
        self._total_rows = self._total_rows + value

    def add_words(self, value: int) -> None:
        self._total_words = self._total_words + value


class DataConsumer:
    def __init__(self, queue_files: Queue):
        self._queue_files: Queue[list[str]] = queue_files
        self._data_transform = DataTransform()

    @property
    def queue_files(self) -> Queue[list[str]]:
        return self._queue_files

    @property
    def data_transform(self) -> DataTransform:
        return self._data_transform

    def calc_rows(self, text: list[str]) -> None:
        self._data_transform.add_rows(value=len(text))

    def calc_words(self, text: list[str]) -> None:
        for string in text:
            self._data_transform.add_words(value=len(string.split()))

    def calc_rows_and_words(self) -> None:
        while True:
            try:
                text: list[str] = self.queue_files.get()
            except Empty:
                print("Очередь пуста;")
                continue
            else:
                self.calc_rows(text=text)
                self.calc_words(text=text)
                self.queue_files.task_done()

def main():
    # Создание очереди для текстового содержимого из файлов;
    queue_files: Queue = Queue()

    # Создание и запуск потока-производителя;
    producer = DataProducer(queue_files=queue_files)
    thread_producer: Thread = Thread(
            target=producer.put_data_in_queue,
            daemon=True
    )
    thread_producer.start()
    thread_producer.join()

    # Создание и запуск потока-потребителя;
    consumer: DataConsumer = DataConsumer(queue_files=queue_files)
    thread_consumer: Thread = Thread(
            target=consumer.calc_rows_and_words,
            daemon=True
    )
    thread_consumer.start()
    queue_files.join()

    print(
        f"Суммарное количество строк: {consumer.data_transform.total_rows}",
        f"Суммарное количество слов: {consumer.data_transform.total_words}",
        sep="\n"
    )

if __name__ == "__main__":
    main()
