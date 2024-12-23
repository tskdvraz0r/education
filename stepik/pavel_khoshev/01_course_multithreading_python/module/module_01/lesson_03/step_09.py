# Импорты
import sys
import threading

from typing import List, Union

from loguru import logger

# Настройка логирования
logger.remove()
logger.add(sink=sys.stderr, level="TRACE")

# Определяем функции для сортировки массивов
def sort_descending(array: List[Union[int, str]]) -> None:
    """
    Сортирует массив в порядке убывания.
    :param array: Массив для сортировки.
    """
    if not isinstance(array, list):
        logger.error("Ошибка: входные данные не являются списком")
        sys.exit(1)

    try:
        logger.trace(f"Сортировка массива в порядке убывания: {array}")
        array.sort(reverse=True)
        logger.trace(f"Массив отсортирован в порядке убывания: {array}")
    except Exception as e:
        logger.error(f"Ошибка при сортировке массива в порядке убывания: {e}")
        sys.exit(1)

def sort_ascending(array: List[Union[int, str]]) -> None:
    """
    Сортирует массив в порядке возрастания.
    :param array: Массив для сортировки.
    """
    if not isinstance(array, list):
        logger.error("Ошибка: входные данные не являются списком")
        sys.exit(1)

    try:
        logger.trace(f"Сортировка массива в порядке возрастания: {array}")
        array.sort()
        logger.trace(f"Массив отсортирован в порядке возрастания: {array}")
    except Exception as e:
        logger.error(f"Ошибка при сортировке массива в порядке возрастания: {e}")
        sys.exit(1)

def sort_symbols(array: List[str]) -> None:
    """
    Сортирует массив символов в лексикографическом порядке.
    :param array: Массив символов для сортировки.
    """
    if not isinstance(array, list):
        logger.error("Ошибка: входные данные не являются списком")
        sys.exit(1)

    try:
        logger.trace(f"Сортировка массива символов: {array}")
        array.sort()
        logger.trace(f"Массив символов отсортирован: {array}")
    except Exception as e:
        logger.error(f"Ошибка при сортировке массива символов: {e}")
        sys.exit(1)

# Определяем массивы
array_descending: List[int] = [733, 725, 606, 544, 526, 496, 448, 389, 345, 239]
array_ascending: List[int] = [124, 168, 350, 389, 419, 428, 501, 662, 760, 829]
symbols_array: List[str] = ['g', 'e', 'k', 'a', 'w', 'z', 'o', 'b', 'm', 'l', 'h', 'n', 'd', 's', 'q']

# Создаем потоки
thread1 = threading.Thread(target=sort_descending, args=(array_descending,))
thread2 = threading.Thread(target=sort_ascending, args=(array_ascending,))
thread3 = threading.Thread(target=sort_symbols, args=(symbols_array,))

# Запускаем потоки
try:
    thread1.start()
    thread2.start()
    thread3.start()
except Exception as e:
    logger.error(f"Ошибка при запуске потоков: {e}")
    sys.exit(1)

# Ждем завершения всех потоков
try:
    thread1.join()
    thread2.join()
    thread3.join()
except Exception as e:
    logger.error(f"Ошибка при ожидании завершения потоков: {e}")
    sys.exit(1)

# Выводим отсортированные массивы
print(f"Массив чисел (по убыванию): {array_descending}")
print(f"Массив чисел (по возрастанию): {array_ascending}")
print(f"Массив символов (лексикографический порядок): {symbols_array}")