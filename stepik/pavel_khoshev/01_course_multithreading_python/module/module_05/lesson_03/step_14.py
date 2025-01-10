from __init__ import ROOT_FOLDER_PATH

import sys
from time import sleep
from random import random
from threading import Event
from concurrent.futures import ThreadPoolExecutor

sys.path.append(ROOT_FOLDER_PATH)
from packages.utils.decorators.time_spend import time_spend


CLIENTS: list[str] = ["Виктор", "Ирина", "Андрей"]
event_cashier: Event = Event()

def client(client_name: str) -> None:
    print(f"{client_name} вошел в банк")
    event_cashier.wait()
    print(f"{client_name} обслужен и покидает банк")


def cashier(client_name: Event) -> None: 
    print(f"Обслуживаю клиента {client_name}")
    sleep(random())
    print(f"Клиент {client_name} обслужен")
    event_cashier.set()


@time_spend
def main() -> None:
    
    with ThreadPoolExecutor() as executor:
        for client_name in CLIENTS:
            executor.submit(client, client_name)
            executor.submit(cashier, client_name)
    
    print("Все клиенты обслужены. Банк закрывается.")
        

if __name__ == "__main__":
    main()
