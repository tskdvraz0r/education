import time
from concurrent.futures import ThreadPoolExecutor


# Создайте целевую функцию;
def print_from_one_to_five() -> None:
    for i in range(1, 6):
        time.sleep(0.5)
        print(i)


def print_from_a_to_e() -> None:
    for i in "abcde":
        time.sleep(1)
        print(i)


def main() -> None:
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(print_from_one_to_five)
        executor.submit(print_from_a_to_e)
    
    print("Готово!")


if __name__ == "__main__":
    main()
