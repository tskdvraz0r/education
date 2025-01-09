from sys import platform
from json import dump
from queue import Queue
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


list_queues_lock: Lock = Lock()
result_lock: Lock = Lock()

match platform:
    case "win32":
        data_folder: str = r"C:\Users\d.zakharchenko\Desktop\GitHub\education\stepik\pavel_khoshev\01_course_multithreading_python\module\module_05\lesson_01\data\step_14\\"
        encoding: str = "utf-8"
    case "darwin":
        data_folder: str = ""
        encoding: str = "latin1"


files_names: list[str] = [
    "first_name",
    "last_name",
    "age",
    "country",
    "hobbies",
    "salary",
    "job_title",
    "email",
    "projects",
    "education",
]


class DataExtractor:
    
    @classmethod
    def run(cls, filename: str) -> None:
        with open(
            file=rf"{data_folder}{filename}.txt",
            mode="r",
            encoding=encoding,
        ) as file:
            return list(map(str.strip, file.readlines()))


class DataLoader:

    @classmethod
    def run(cls, data) -> None:
        with result_lock:
            with open(
                file=rf"{data_folder.replace("\step_14", "")}_result.json",
                mode="w",
                encoding=encoding,
            ) as file:
                dump(data, file, ensure_ascii=False, indent=4)


class DataProducer:
    
    def __init__(self, queues: list) -> None:
        self.queues: list = queues
    
    def run(self, filename: str) -> None:
        with list_queues_lock:
            temp_queue: Queue[str] = Queue()
            data_extractor: DataExtractor = DataExtractor()
            
            for row in data_extractor.run(filename):
                temp_queue.put(row)
            self.queues.append(temp_queue)


class DataConsumer:
    
    def __init__(self, queues: list) -> None:
        self.queues: list = queues
    
    def run(self) -> None:
        result: list = []
        for _ in range(self.queues[0].qsize()):
            values: list = []
            for queue in self.queues:
                values.append(queue.get())
                queue.task_done()
            result.append(dict(zip(files_names, values)))
        DataLoader.run(data=result)


def main() -> None:
    # Список для экземпляров класса очереди;
    queues: list = []
    
    # Создание экземпляра класса DataProducer;
    data_producer: DataProducer = DataProducer(queues=queues)
    
    # Создание экземпляра класса DataConsumer;
    data_consumer: DataConsumer = DataConsumer(queues=queues)
    
    with ThreadPoolExecutor() as executor:
        executor.map(data_producer.run, files_names)
    
    data_consumer.run()
    queues[0].join()


if __name__ == "__main__":
    main()
