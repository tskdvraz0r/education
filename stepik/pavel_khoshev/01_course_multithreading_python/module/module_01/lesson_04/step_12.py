import threading as thr

# Получить объект главного потока;
main_thread: thr.Thread = thr.main_thread()

# Вывести имя главного потока по умолчанию;
print(f"Имя главного потока по умолчанию: {main_thread.name}")

# Установить новое имя главного потока и вывести в стандартный поток;
main_thread.name = "My_main_thread"
print(f"Новое имя главного потока: {main_thread.name}")

# Вывести демонический признак главного потока;
print(f"Демонический признак главного потока: {main_thread.daemon}")