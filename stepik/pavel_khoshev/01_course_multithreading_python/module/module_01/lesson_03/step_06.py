# Импорты
import sys
import typing
import threading as thr

from loguru import logger


# Настройка логирования;
logger.remove()
logger.add(sys.stderr, level="TRACE")

# Константы;
LIST_WITH_NUMBERS: typing.Final[list[int]] = [123456, 7890123, 987654, 114455, 995423, 1000000]

# Глобальные переменные;
total_sum: int = 0
logger.trace("Глобальная переменная total_sum инициализирована.")

# Целевая функция; 
def sum_of_numbers() -> None:
    """
    Суммирует числа из списка LIST_WITH_NUMBERS и сохраняет результат в глобальной переменной total_sum.
    """
    global total_sum
    logger.trace("Начало суммирования чисел.")
    
    try:
        for number in LIST_WITH_NUMBERS:
            total_sum += number
            logger.trace(f"Добавлено число {number}, текущая сумма: {total_sum}")
    except Exception as e:
        logger.error(f"Произошла ошибка при суммировании чисел: {e}")
        sys.exit(1)
    
    logger.trace("Суммирование чисел завершено.")

# Функция для потока, обрабатывающего список чисел;
def thread_task() -> None:
    """
    Запускает функцию sum_of_numbers в отдельном потоке.
    """
    logger.trace("Запуск потока для суммирования чисел.")
    try:
        sum_of_numbers()
    except Exception as e:
        logger.error(f"Произошла ошибка в потоке: {e}")
        sys.exit(1)

    logger.trace("Поток завершил работу.")

# Создание потока;
thread: thr.Thread = thr.Thread(target=thread_task)

# Запуск потока;
logger.trace("Запуск основного потока.")
try:
    thread.start()
except Exception as e:
    logger.error(f"Произошла ошибка при запуске потока: {e}")
    sys.exit(1)

# Ожидание завершения потока;
try:
    thread.join()
except Exception as e:
    logger.error(f"Произошла ошибка при ожидании завершения потока: {e}")
    sys.exit(1)

# Вывод результата;
logger.trace(f"Общая сумма чисел: {total_sum}")
print(total_sum)