import sys
import threading as thr

from loguru import logger


# Настройка логирования
logger.remove()
logger.add(sys.stdout, level="TRACE")

# Переменные;
total_sum: int = 0
total_prod: int = 1

# Локальные функции;
def sum_of_numbers() -> None:
    """
    Вычисляет сумму чисел от 1 до 1000 и сохраняет результат в глобальной переменной total_sum.
    """
    global total_sum
    try:
        logger.trace("Начало вычисления суммы чисел от 1 до 1000")
        total_sum = sum(range(1, 1001))
        logger.trace(f"Сумма чисел от 1 до 1000: {total_sum}")
    except Exception as e:
        logger.error(f"Ошибка при вычислении суммы чисел: {e}")
        sys.exit(1)

def prod_of_numbers() -> None:
    """
    Вычисляет произведение чисел от 1 до 10 и сохраняет результат в глобальной переменной total_prod.
    """
    global total_prod
    try:
        logger.trace("Начало вычисления произведения чисел от 1 до 10")
        for i in range(1, 11):
            total_prod *= i
        logger.trace(f"Произведение чисел от 1 до 10: {total_prod}")
    except Exception as e:
        logger.error(f"Ошибка при вычислении произведения чисел: {e}")
        sys.exit(1)

# Создать потоки;
logger.trace("Создание потоков")
thr_sum: thr.Thread = thr.Thread(target=sum_of_numbers)
thr_prod: thr.Thread = thr.Thread(target=prod_of_numbers)

# Запустить потоки;
logger.trace("Запуск потоков")
thr_sum.start()
thr_prod.start()

# Дождаться завершения потоков;
logger.trace("Ожидание завершения потоков")
thr_sum.join()
thr_prod.join()

# Вывести результат;
logger.trace("Вывод результатов")
try:
    print(
        f"Сумма чисел от 1 до 1000: {total_sum}",
        f"Произведение чисел от 1 до 10: {total_prod}",
        sep="\n"
    )
except Exception as e:
    logger.error(f"Ошибка при выводе результатов: {e}")
    sys.exit(1)