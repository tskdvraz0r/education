import threading as th

initial_bid: int = 0
bid_increment: int = 1
max_bid: int = 10
interval: int = 1
current_bid: int = initial_bid


def increase_bid(bid_increment: int, max_bid: int, interval: int) -> None:
    global current_bid

    if current_bid < max_bid:
        current_bid += bid_increment
        print(f"Текущая ставка: {current_bid} у.е.")

        th.Timer(
            interval=interval,
            function=increase_bid,
            kwargs={
                "bid_increment": bid_increment,
                "max_bid": max_bid,
                "interval": interval,
            },
        ).start()

    else:
        print("Ставок нет, аукцион завершен!")


thread: th.Thread = th.Thread(
    target=increase_bid,
    kwargs={"bid_increment": bid_increment, "max_bid": max_bid, "interval": interval},
)
thread.start()
thread.join()
