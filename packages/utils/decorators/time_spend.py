import time
from typing import Any


def time_spend(func): # type: ignore
    """
    Декоратор, который измеряет время выполнения функции.

    Args:
        func (typing.Callable): Функция, время выполнения которой нужно измерить.

    Returns:
        typing.Callable: Декорированная функция.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Обертка для функции, которая измеряет время ее выполнения.

        Args:
            *args: Позиционные аргументы функции.
            **kwargs: Именованные аргументы функции.

        Returns:
            typing.Any: Результат выполнения функции.
        """

        # Время начала выполнения функции/метода;
        start_time: float = time.time()

        # Результат выполнения функции/метода;
        result: Any = func(*args, **kwargs)

        # Время окончания выполнения функции;
        finish_time: float = time.time()

        # Затрачено времени;
        print(f"Время выполнения функции: {finish_time - start_time}")

        return result

    return wrapper
