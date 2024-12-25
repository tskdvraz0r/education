import time
import typing
import threading as th


students_info: dict[str, dict[str, typing.Any]] = {
    "Варлаам Бирюкова": {
        "Возраст": 25,
        "Специальность": None,
        "Город": None,
        "Страна": "Россия",
        "Университет": "ЗАО «Миронова-Прохоров»",
        "Курс": 3,
        "Группа": "CK008",
        "Электронная почта": "ostaplitkin@example.com",
        "Телефон": None,
        "Дата рождения": "2005-08-22",
        "Пол": "Женский",
        "Хобби": ["Физика", "Астрономия"],
        "Время обработки": 6,
    },
    "Никандр Мамонтов": {
        "Возраст": 20,
        "Специальность": "Компьютерные науки",
        "Город": "к. Октябрьский (Башк.)",
        "Страна": "Россия",
        "Университет": None,
        "Курс": 3,
        "Группа": "LE057",
        "Электронная почта": "jakub_2001@example.org",
        "Телефон": "+7 919 424 9512",
        "Дата рождения": "2002-01-13",
        "Пол": None,
        "Хобби": None,
        "Время обработки": 5,
    },
}


local_storage = th.local()


def thread_function(
    student_name: str, student_info: dict[str, typing.Any], process_time: int = 3
) -> None:
    thread: th.Thread = th.current_thread()
    thread.name = student_name

    local_storage.data = student_info

    if (
        "Время обработки" in local_storage.data.keys()
        and local_storage.data["Время обработки"] is not None
    ):
        time.sleep(local_storage.data["Время обработки"] / 10)
    else:
        time.sleep(process_time / 10)

    for key, value in local_storage.data.items():
        if value is not None:
            print(
                f"Имя потока - {thread.name}, локальные данные потока - {key}: {value}"
            )


for student_name, student_info in students_info.items():
    thread = th.Thread(target=thread_function, args=(student_name, student_info))
    thread.start()
    time.sleep(0.1)
