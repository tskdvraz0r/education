import threading as thr
from typing import List

import pytest
from loguru import logger

from module.module_01.lesson_03 import step_06

# Тесты для функции sum_of_numbers
@pytest.mark.parametrize("numbers, expected_sum", [
   ([1, 2, 3], 6),
   ([10, 20, 30], 60),
   ([100, 200, 300], 600),
])
def test_sum_of_numbers(numbers: List[int], expected_sum: int):
   global total_sum
   total_sum = 0
   step_06.LIST_WITH_NUMBERS = numbers
   logger.trace("Начало теста sum_of_numbers")
   step_06.sum_of_numbers()
   logger.trace(f"Ожидаемая сумма: {expected_sum}, текущая сумма: {total_sum}")
   assert total_sum == expected_sum
   logger.trace("Тест sum_of_numbers завершен")

# Тесты для функции thread_task
@pytest.mark.parametrize("numbers, expected_sum", [
   ([1, 2, 3], 6),
   ([10, 20, 30], 60),
   ([100, 200, 300], 600),
])
def test_thread_task(numbers: List[int], expected_sum: int):
   global total_sum
   total_sum = 0
   step_06.LIST_WITH_NUMBERS = numbers
   logger.trace("Начало теста thread_task")
   thread = thr.Thread(target=step_06.thread_task)
   thread.start()
   thread.join()
   logger.trace(f"Ожидаемая сумма: {expected_sum}, текущая сумма: {total_sum}")
   assert total_sum == expected_sum
   logger.trace("Тест thread_task завершен")
