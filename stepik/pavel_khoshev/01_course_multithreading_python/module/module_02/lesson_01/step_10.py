from concurrent.futures import Future, ThreadPoolExecutor


start_and_end: tuple[tuple[int, int]] = (
    (1, 101),
    (101, 201),
    (201, 301)
)


def sum_range(start, end) -> int:
    return sum(range(start, end))


with ThreadPoolExecutor(max_workers=3) as executor:
    futures: list[Future[int]] = [executor.submit(sum_range, *ranges) for ranges in start_and_end]
    
    sum1, sum2, sum3 = [future.result() for future in futures]


print(f"Сумма чисел от 1 до 100: {sum1}")
print(f"Сумма чисел от 101 до 200: {sum2}")
print(f"Сумма чисел от 201 до 300: {sum3}")