import time
import threading as t

oven_lock = t.Lock()

cooks_names = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]
pizzas = {
    "Маргарита": 3,
    "Пепперони": 2,
    "Вегетарианская": 4,
    "Четыре сыра": 5,
    "Гавайская": 3
}

def create_pizze(cook: str, pizza_delay: tuple) -> None:
    pizza, delay = pizza_delay
    with oven_lock:
        print(f'{cook} начал(а) готовить пиццу "{pizza}".')
        time.sleep(delay)
        print(f'{cook} закончил(а) готовить пиццу "{pizza}".')

def main() -> None:
    threads = [
        t.Thread(target=create_pizze, args=(cook, pizza_delay))
        for cook, pizza_delay in zip(cooks_names, pizzas.items())
    ]

    for thread in threads:
        thread.start()
        thread.join()

    print("Все пиццы приготовлены!")

if __name__ == "__main__":
    main()