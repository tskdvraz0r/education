from threading import Lock
from concurrent.futures import ThreadPoolExecutor

products = {
    1: {"name": "Компьютер ProMax", "price": 50000, "stock": 1},
    2: {"name": "Телефон UltraTalk", "price": 30000, "stock": 1},
    3: {"name": "Наушники SoundBeats", "price": 2000, "stock": 0},
    4: {"name": "Планшет ViewTab", "price": 15000, "stock": 20},
    5: {"name": "Монитор ClearView", "price": 10000, "stock": 15},
    6: {"name": "Клавиатура QuickType", "price": 1500, "stock": 30},
    7: {"name": "Мышь Clicker", "price": 800, "stock": 40},
    8: {"name": "Флешка SpeedDrive", "price": 500, "stock": 0},
    9: {"name": "Жесткий диск StoreMore", "price": 4000, "stock": 25},
    10: {"name": "Принтер PrintAll", "price": 6000, "stock": 12},
    11: {"name": "Смартфон FlexPhone", "price": 25000, "stock": 18},
    12: {"name": "Ноутбук CarryComp", "price": 45000, "stock": 8},
    13: {"name": "Камера SnapShot", "price": 8000, "stock": 22},
    14: {"name": "Проектор LightShow", "price": 12000, "stock": 0},
    15: {"name": "Спикеры SoundWave", "price": 2500, "stock": 35},
    16: {"name": "Монопод SelfieStick", "price": 700, "stock": 60},
    17: {"name": "Роутер NetFast", "price": 3000, "stock": 28},
    18: {"name": "Планшет SketchTab", "price": 13000, "stock": 0},
    19: {"name": "Микрофон EchoMic", "price": 1500, "stock": 45},
    20: {"name": "Веб-камера VisionPro", "price": 2000, "stock": 0},
    21: {"name": "Наушники BassHead", "price": 1800, "stock": 55},
    22: {"name": "Мышь для геймеров GameMaster", "price": 1200, "stock": 38},
    23: {"name": "Клавиатура для геймеров KeyStrike", "price": 2500, "stock": 0},
    24: {"name": "Графический планшет DrawMaster", "price": 8000, "stock": 17},
    25: {"name": "Смарт-часы TimeTech", "price": 3000, "stock": 23},
    26: {"name": "Компьютерные колонки SoundSpace", "price": 3500, "stock": 30},
    27: {"name": "Беспроводная мышь FreedomClick", "price": 1000, "stock": 42},
    28: {"name": "Смартфон Samsung GalaxyZ", "price": 27000, "stock": 0},
    29: {"name": "Смартфон iPhone X", "price": 35000, "stock": 9},
    30: {"name": "Ноутбук Dell Inspire", "price": 48000, "stock": 7},
}


def search_product(id: int):

    print(f"Поиск товара: {products[id]['name']}")
    if "stock" not in products[id].keys() or products[id]["stock"] == 0:
        with Lock():
            print(f"Товар ID {id} не найден или закончился на складе.")
    else:
        with Lock():
            print(f"Товар ID: {id} {products[id]}")


def is_task_done(future):
    with Lock():
        print(f'Поиск завершён, статус: {future.done()}')

def total_stock_cost():
    total_cost: int = 0
    for id in products.keys():
        total_cost += products[id]["price"] * products[id]["stock"]
    with Lock():
        print(f"Общая стоимость товаров на складе: {total_cost}")


with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(search_product, product_id)
        for product_id in products.keys()
    ]
    for future in futures:
        future.add_done_callback(is_task_done)

total_stock_cost()