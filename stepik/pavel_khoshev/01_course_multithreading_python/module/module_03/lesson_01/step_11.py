from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep

timeouts = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
numbers = [2257, 6217, 6594, 2259, 5284, 3568, 1741, 5462, 7494, 8971, 3157, 3998, 2040, 8828, 8769, 6976, 9367, 1267, 6255, 7322]
total_sum = 0

def process_number(timeout: int, number: int) -> int:
    sleep(timeout)
    return number


with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
    futures = [executor.submit(process_number, timeout, number) for timeout, number in zip(
        timeouts, numbers)]
    done, not_done = wait(futures, timeout=3)

    for result in done:
        total_sum += result.result()

print(total_sum)
