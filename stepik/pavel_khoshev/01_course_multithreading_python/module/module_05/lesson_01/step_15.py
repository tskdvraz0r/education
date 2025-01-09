import os
import sys
from threading import Lock
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait


lock_queue_files_names: Lock = Lock()
lock_result_file: Lock = Lock()


class DataExtractor:
    
    def __init__(self) -> None:
        match sys.platform:
            case "win32":
                self.data_folder: str = r"stepik\pavel_khoshev\01_course_multithreading_python\module\module_05\lesson_01\data\step_15\\"
            case "darwin":
                pass
            case _:
                raise NotImplementedError("Данная ОС не поддерживается;")
        self.files_names: Queue[str] = Queue()
    
    
    def get_files_names(self) -> list[str]:
        return os.listdir(self.data_folder)


    def run(self, queue: Queue[int], filename: str) -> None:
    
        with open(
            file=rf"{self.data_folder}{filename}",
            mode="r",
            encoding="utf-8",
        ) as file:
            queue.put(file.readlines())


class DataLoader:
    
    def __init__(self) -> None:
        match sys.platform:
            case "win32":
                self.data_folder: str = r"stepik\pavel_khoshev\01_course_multithreading_python\module\module_05\lesson_01\data\\"
            case "darwin":
                pass
            case _:
                raise NotImplementedError("Данная ОС не поддерживается;")
    
    def load_to_txt(self, data: int) -> None:
        with open(
            file=rf"{self.data_folder}_result.txt",
            mode="a",
            encoding="utf-8",
        ) as file:
            file.write(f"{data}\n")


class DataProducer:
    
    def __init__(self) -> None:
        self.queue: Queue = Queue()
    
    
    def process_file_data(self, data: str) -> int:
        return int(data) * 3 / 4
    
    
    def run(self, queue_process: Queue, queue_src: Queue):
        while not queue_src.empty():
            item = list(map(self.process_file_data, queue_src.get()))
            queue_process.put(sum(item))
            queue_src.task_done()


class DataConsumer:
    
    def run(self, data_loader: DataLoader, queue_result: Queue) -> None:
        while not queue_result.empty():
            item = queue_result.get()
            with lock_result_file:
                data_loader.load_to_txt(data=item)
            queue_result.task_done()


def main() -> None:
    # Создание экземпляров класса Queue;
    queue_src_data: Queue = Queue()
    queue_processed_data: Queue = Queue()
    
    # Создание экземпляра класса DataExtractor;
    data_extractor: DataExtractor = DataExtractor()
    data_producer: DataProducer = DataProducer()
    data_consumer: DataConsumer = DataConsumer()
    data_loader: DataLoader = DataLoader()
    
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(data_extractor.run, queue=queue_src_data, filename=filename)
            for filename in data_extractor.get_files_names()
        ]
        
        wait(futures, return_when="ALL_COMPLETED")

        executor.submit(data_producer.run, queue_process=queue_processed_data, queue_src=queue_src_data)
        queue_src_data.join()
        
        executor.submit(data_consumer.run, data_loader=data_loader, queue_result=queue_processed_data)
        queue_processed_data.join()


if __name__ == "__main__":
    main()
