from concurrent.futures import ThreadPoolExecutor


numbers: list[int] = [2, 17, 8, 11, 14, 5]


def get_square_of_number(number: int) -> int:
    print(number ** 2)


with ThreadPoolExecutor(max_workers=3) as executor:
    [executor.submit(get_square_of_number, number=i) for i in numbers]
