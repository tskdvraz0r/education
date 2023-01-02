/* Задача 08:
    Из таблицы courier_actions отберите id трёх курьеров, доставивших в сентябре 2022 года наибольшее количество заказов. 
Выведите две колонки — id курьера и число доставленных заказов. Колонку с числом доставленных заказов назовите delivered_orders.

Поля в результирующей таблице: 
courier_id, delivered_orders */

SELECT
    courier_id,
    COUNT(DISTINCT order_id) - COUNT(DISTINCT order_id) FILTER (WHERE action = 'cancel_order') AS delivered_orders

FROM courier_actions
    WHERE DATE_PART('month', time) = 9

GROUP BY 
    courier_id

ORDER BY 
    delivered_orders DESC

LIMIT 3

-- 2
SELECT
    courier_id,
    COUNT(DISTINCT order_id) FILTER (WHERE action = 'deliver_order') AS delivered_orders

FROM courier_actions
    WHERE DATE_PART('month', time) = 9

GROUP BY 
    courier_id

ORDER BY 
    delivered_orders DESC

LIMIT 3