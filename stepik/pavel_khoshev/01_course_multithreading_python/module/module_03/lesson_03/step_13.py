from concurrent.futures import ThreadPoolExecutor
from time import sleep


data = [
    (1, "Python"),
    (2, "Java"),
    (3, "Go"),
    (4, "JavaScript"),
    (5, "C++"),
    (6, "TypeScript"),
    (7, "PHP"),
    (8, "Ruby"),
    (9, "C"),
    (10, "C#")
]

def programming_languages(ratio: tuple):
    sleep(0.1)
    ratio, language = ratio
    return f"{language} на {ratio}-м месте на GitHub в первом квартале 2024 года"

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(programming_languages, values) for values in data]
    for future in futures:
        print(future.result())
