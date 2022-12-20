/* Задача 3:
Выведите первые 50 строк из таблицы orders. Включите в результат только колонки с id и временем создания заказа.
Поля в результирующей таблице: order_id, creation_time. */

SELECT
    order_id,
    creation_time

FROM orders

LIMIT 50