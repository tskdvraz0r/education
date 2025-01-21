import time
import random
from threading import Event
from concurrent.futures import ThreadPoolExecutor, wait

auction_start_painting: Event = Event()
auction_start_clock: Event = Event()

bidder_names: tuple[str] = ("Сергей", "Борис", "Виктор", "Евдоким", "Егор")

def bid(bidder_name: str, event_paiting: Event, event_clock: Event) -> None:
    print(f'Участник {bidder_name} готов к аукциону за редкую картину.')
    print(f'Участник {bidder_name} готов к аукциону за антикварные часы.')
    event_paiting.wait()
    event_clock.wait()
    
    time.sleep(0.25)
    print(f"Участник {bidder_name} делает ставку на редкую картину.")
    print(f"Участник {bidder_name} делает ставку на антикварные часы.")


def main() -> None:
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(bid, bidder, auction_start_painting, auction_start_clock)
            for bidder in bidder_names
        ]
        
        print('Аукцион за редкую картину начинается!')
        auction_start_clock.set()
        print('Аукцион за редкую картину начинается!')
        auction_start_painting.set()

        wait(futures)
        
        print('Аукцион за редкую картину завершился!')
        print('Аукцион за антикварные часы завершился!')
        
        print(f"Победитель аукциона за редкую картину: {random.choice(bidder_names)}")
        print(f"Победитель аукциона за антикварные часы: {random.choice(bidder_names)}")

if __name__ == '__main__':
    main()
