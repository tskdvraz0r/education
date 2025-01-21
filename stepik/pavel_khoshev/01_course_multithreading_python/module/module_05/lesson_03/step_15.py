from threading import Event
from concurrent.futures import ThreadPoolExecutor

BIDDER_NAMES: tuple[str] = ("Сергей", "Борис", "Виктор", "Евдоким", "Егор")

event_bid: Event = Event()

def bid(bidder_name: str, event: Event) -> None:
    print(f'Участник {bidder_name} готов к аукциону.')
    event.wait()
    print(f'Участник {bidder_name} делает ставку на редкую картину.')

def main() -> None:
    with ThreadPoolExecutor() as executor:
        for bidder_name in BIDDER_NAMES:
            executor.submit(bid, bidder_name, event_bid)
        print('Аукцион начинается!')
        event_bid.set()

if __name__ == "__main__":
    main()
