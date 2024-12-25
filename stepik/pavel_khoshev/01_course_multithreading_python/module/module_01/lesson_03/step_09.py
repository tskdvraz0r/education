import threading as th


array_descending: list[int] = [
    733, 725, 606, 544,
    526, 496, 448, 389,
    345, 239
]
array_ascending: list[int] = [
    124, 168, 350, 389,
    419, 428, 501, 662,
    760, 829
]
array_symbols: list[str] = [
    "g", "e", "k", "a", "w",
    "z", "o", "b", "m", "l",
    "h", "n", "d", "s", "q"
]


def sort_descending(array: list[int] | list[str]) -> None:
    array.sort(reverse=True)


def sort_ascending(array: list[int] | list[str]) -> None:
    array.sort()


thread1: th.Thread = th.Thread(target=sort_descending, args=(array_descending,))
thread2: th.Thread = th.Thread(target=sort_ascending, args=(array_ascending,))
thread3: th.Thread = th.Thread(target=sort_ascending, args=(array_symbols,))


thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()


print(f"Массив чисел (по убыванию): {array_descending}")
print(f"Массив чисел (по возрастанию): {array_ascending}")
print(f"Массив символов (лексикографический порядок): {array_symbols}")
