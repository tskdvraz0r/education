from string import punctuation
from collections import Counter
from concurrent.futures import ThreadPoolExecutor


messages: list[str] = [
    "Привет, коллеги! Кто-нибудь может объяснить разницу между асинхронным и многопоточным программированием в Python?",
    "Асинхронное программирование позволяет обрабатывать несколько задач без блокировки основного потока.",
    "Многопоточное программирование также обеспечивает параллельное выполнение, но с использованием потоков вместо асинхронных задач.",
    "Помните, что асинхронное программирование может требовать пересмотра структуры кода и логики приложения.",
    "Многопроцессорное программирование может использовать модуль multiprocessing.Event для организации событийного взаимодействия между процессами.",
    "Асинхронные функции могут использовать asyncio.ensure_future() для запуска задачи в асинхронном режиме.",
]
letter_values: dict[str, int] = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5,
    'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10,
    'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15,
    'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20,
    'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25,
    'ш': 26, 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30,
    'э': 31, 'ю': 32, 'я': 33
}

result = ("", 0)


def sum_letters(string: str) -> None:
    global result
    
    # Исходная строка;
    src_string: str = string
    
    # Обрабатываемая строка;
    temp_string: str = string.lower()
    
    # Удалить из строки знаки пунктуации и цифры;
    for char in punctuation + " 0123456789":
        temp_string = temp_string.replace(char, "")
    
    # Подсчитать количество букв в строке;
    counter = Counter(temp_string)
    
    # Подсчитать сумму строки;
    sum_string: int = 0
    for key, value in counter.items():
        sum_string += letter_values[key] * value
    
    if sum_string > result[1]:
        result = (src_string, sum_string)


with ThreadPoolExecutor() as executor:
    executor.map(sum_letters, messages)

print(result[0])
