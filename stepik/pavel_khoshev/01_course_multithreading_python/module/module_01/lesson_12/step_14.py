import time
import threading as th

aircrafts = {
    "Boeing 737": 6,
    "Airbus A320": 9,
    "Boeing 747": 6,
    "Airbus A380": 7,
}


def flight_simulation(
    aircraft: str,
    flight_time: int,
) -> None:
    print(f"{aircraft} начал полет. Время полета: {flight_time} сек.")
    time.sleep(flight_time)
    print(f"{aircraft} завершил полет.")


def print_count_active_threads() -> None:
    print(f"Количество самолетов в воздухе после 5 секунд: {th.active_count() - 2}")


for aircraft, flight_time in aircrafts.items():
    th.Thread(target=flight_simulation, args=(aircraft, flight_time)).start()

th.Timer(interval=5, function=print_count_active_threads).start()
