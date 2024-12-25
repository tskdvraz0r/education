from concurrent.futures import Future, ThreadPoolExecutor


list1: list[str] = ["kw63vdxI", "YmSsWblC", "5OJ3Mto9"]
list2: list[str] = ["7GBrUY6t", "bfQjS3gj", "MhTsKf0X"]
list3: list[str] = ["mt05f80F", "haHHiXoX", "v2cYPhRO"]


def worker(texts: list[str], thread_num: int) -> None:
    for string in texts:
        print(f"Поток {thread_num} извлёк текст из списка: {string}")


with ThreadPoolExecutor(max_workers=3) as executor:
    for idx, data in zip((1, 2, 3), (list1, list2, list3)):
        future: Future = executor.submit(worker, texts=data, thread_num=idx)
