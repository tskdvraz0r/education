from concurrent.futures import ThreadPoolExecutor
import random as rd

# Определяем границы для разделения массива
limits = [(1, 300), (301, 500), (501, 700), (701, 999)]

# Генерируем случайные числа
numbers = [rd.randrange(1, 1000) for _ in range(150)]


# Функция для разделения массива на подмассивы
def divide_array(array: list) -> list:
    sub_arrays = [[] for _ in range(len(limits))]
    for i in array:
        for j, (lower, upper) in enumerate(limits):
            if lower <= i <= upper:
                sub_arrays[j].append(i)
                break
    return sub_arrays


# Функция для сортировки подмассивов
def sort_array(array: list, limits: tuple[int, int]) -> str:
    array.sort()
    return f"Числа в массиве от {limits[0]} до {limits[1]} {array}"


# Разделяем массив на подмассивы
sub_arrays = divide_array(numbers)

# Сортируем подмассивы с помощью ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    results = executor.map(sort_array, sub_arrays, limits)

# Выводим результаты
for result in results:
    print(result)
