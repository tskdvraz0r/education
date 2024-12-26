from typing import Any, Iterator
from concurrent.futures import ThreadPoolExecutor


students = {
    1: {"name": "Alice", "age": 20, "grades": [4, 5, 5, 4, 2, 3, 5, 2]},
    2: {"name": "Bob", "age": 21, "grades": [3, 4, 3, 4, 4, 5, 3, 4, 3, 2, 4]},
    3: {"name": "Charlie", "age": 19, "grades": [5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 4]},
    # ...
    20: {
        "name": "Hannah Thompson",
        "age": 20,
        "grades": [2, 4, 3, 5, 3, 3, 2, 4, 4, 3, 2, 2, 2, 2, 5, 3, 4, 5],
    },
}


def calculate_average(student):
    grades = student["grades"]
    average = sum(grades) / len(grades)
    return student["name"], round(average, 2)


with ThreadPoolExecutor(max_workers=5) as executor:
    results: Iterator[tuple[Any, float]] = executor.map(
        calculate_average, students.values()
    )

average_grades = dict(results)
print(average_grades)
