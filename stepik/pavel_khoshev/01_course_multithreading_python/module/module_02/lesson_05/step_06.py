from concurrent.futures import ThreadPoolExecutor


bases: list[int] = [3, 44, 22, 4, 43]
exponents: list[int] = [12, 31, 23, 2, 43]


def power(base: int, exponent: int) -> int:
    print(f"{base} в степени {exponent} равно {base ** exponent}")


with ThreadPoolExecutor() as executor:
    executor.map(power, bases, exponents)