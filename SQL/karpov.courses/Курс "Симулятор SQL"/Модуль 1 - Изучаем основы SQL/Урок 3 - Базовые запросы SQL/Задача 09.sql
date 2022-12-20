/* Задача 9:
Для первых 200 записей из таблицы orders выведите информацию в следующем виде (обратите внимание на пробелы):

Заказ № [id_заказа] создан [дата]

Пример вывода: 
Заказ № 65 создан 2022-09-01

Полученную колонку назовите order_info.

Пояснение:
Чтобы извлечь дату из значений в колонке creation_time, достаточно применить к ней функцию DATE или изменить её тип на DATE:

SELECT DATE(time)
SELECT CAST(time AS DATE)
SELECT time::DATE */

SELECT
    CONCAT('Заказ № ', order_id, ' создан ', creation_time::DATE) AS order_info

FROM orders

LIMIT 200