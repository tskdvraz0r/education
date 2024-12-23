import threading
import sys
from loguru import logger
from typing import List

# Настройка библиотеки loguru
logger.remove()
logger.add(sys.stderr, level="TRACE")

numbers: List[int] = [
   456, 467, 961, 561, 512, 740, 6412, 464, 444, 102, 456, 347, 905, 854, 901, 326,
   267, 236, 790, 235, 745, 769, 467, 734, 745, 895, 445, 312, 123, 451, 523,
   567, 344, 234
]

# Глобальные переменные для хранения сумм
sum_even: int = 0
sum_odd: int = 0

# Функция для суммирования четных чисел
def sum_even_numbers() -> None:
   """
   Функция для суммирования четных чисел в массиве numbers.
   """
   global sum_even
   for num in numbers:
       if isinstance(num, int) and num % 2 == 0:
           sum_even += num

# Функция для суммирования нечетных чисел
def sum_odd_numbers() -> None:
   """
   Функция для суммирования нечетных чисел в массиве numbers.
   """
   global sum_odd
   for num in numbers:
       if isinstance(num, int) and num % 2 != 0:
           sum_odd += num

# Создаем два потока
thread_even = threading.Thread(target=sum_even_numbers)
thread_odd = threading.Thread(target=sum_odd_numbers)

# Запускаем потоки
try:
   logger.trace("Запуск потока для суммирования четных чисел")
   thread_even.start()
   logger.trace("Запуск потока для суммирования нечетных чисел")
   thread_odd.start()
except Exception as e:
   logger.error(f"Ошибка при запуске потоков: {e}")

# Ожидаем завершения потоков
try:
   logger.trace("Ожидание завершения потока для суммирования четных чисел")
   thread_even.join()
   logger.trace("Ожидание завершения потока для суммирования нечетных чисел")
   thread_odd.join()
except Exception as e:
   logger.error(f"Ошибка при ожидании завершения потоков: {e}")

# Выводим результаты
logger.info(f"Сумма четных чисел: {sum_even}")
logger.info(f"Сумма нечетных чисел: {sum_odd}")

print(f"Сумма четных чисел: {sum_even}")
print(f"Сумма нечетных чисел: {sum_odd}")