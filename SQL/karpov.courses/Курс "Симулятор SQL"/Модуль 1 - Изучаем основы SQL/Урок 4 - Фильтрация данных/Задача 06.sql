/* Задача 6:
Напишите SQL-запрос к таблице couriers и выведите всю информацию о курьерах, у которых не указан их день рождения. Результат отсортируйте по возрастанию id.
Поля в результирующей таблице: courier_id, birth_date, sex */

SELECT
    courier_id,
    birth_date,
    sex

FROM couriers
    WHERE birth_date IS null

ORDER BY
    courier_id ASC 