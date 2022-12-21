/* Задача 10:
Из таблицы couriers отберите id всех курьеров, родившихся в период с 1990 по 1995 год включительно. Результат отсортируйте по возрастанию id курьера.
Поле в результирующей таблице: courier_id

Пояснение:
В этой задаче вам может пригодиться функция DATE_PART. Мы рассматривали её на прошлом уроке в этом задании. */

SELECT
    courier_id

FROM couriers
    WHERE DATE_PART('year', birth_date)::VARCHAR BETWEEN '1990' AND '1995'

ORDER BY 
    courier_id ASC