import threading
import time


# Создаем пять объектов Lock, соответствующих пяти духовкам
oven_locks: list[threading.Lock] = [threading.Lock() for _ in range(5)]

dishes: dict[str, dict[str, int]] = {
     'Алексей': {'Маргарита': 3, 'Лазанья': 5, 'Креветочная': 4, 'Мидии в сливках': 4, 'Сицилийская': 5},
     'Марина': {'Мексиканская': 3, 'Вегетарианская': 4},
}


def cook(chief, dish, time_to_cook):
    # Ищем свободную духовку
    for oven_lock in oven_locks:
        if oven_lock.acquire(blocking=False):
            print(f'{chief} начал(а) готовить {dish}, время приготовления {time_to_cook} сек.')
            time.sleep(time_to_cook)
            print(f'{chief} закончил(а) готовить {dish}, заняло {time_to_cook} сек.')
            oven_lock.release()
            return
    
    for oven_lock in oven_locks:
        oven_lock.acquire()
        print(f'{chief} начал(а) готовить {dish}, время приготовления {time_to_cook} сек.')
        time.sleep(time_to_cook)
        print(f'{chief} закончил(а) готовить {dish}, заняло {time_to_cook} сек.')
        oven_lock.release()
        return


# Используем потоки для имитации работы каждого повара
threads: list = []
for chief, dishes_dict in dishes.items():
    for dish, time_to_cook in dishes_dict.items():
        thread = threading.Thread(target=cook, args=(chief, dish, time_to_cook))
        threads.append(thread)
        thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()
