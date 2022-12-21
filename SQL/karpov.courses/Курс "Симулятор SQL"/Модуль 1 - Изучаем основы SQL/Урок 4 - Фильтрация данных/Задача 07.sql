/* Задача 7:
Напишите SQL-запрос к таблице courier_actions, чтобы узнать id и время доставки последних 10 заказов, доставленных курьером с id 100.
Поля в результирующей таблице: order_id, time

Пояснение:
Обратите внимание, что в исходной таблице есть записи не только со временем доставки, но и временем принятия заказа. */

SELECT
    order_id,
    time

FROM courier_actions
    WHERE courier_id = 100
        AND action = 'deliver_order'

ORDER BY 
    time DESC

LIMIT 10