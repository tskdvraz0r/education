/* Задача 09:
А теперь отберите id только тех курьеров, которые в сентябре 2022 года успели доставить только по одному заказу. 
Таблица та же — courier_actions. Вновь выведите две колонки — id курьера и число доставленных заказов. 
Колонку с числом заказов назовите delivered_orders. Результат отсортируйте по возрастанию id курьера.

Поля в результирующей таблице: 
courier_id, delivered_orders */

SELECT
    courier_id,
    COUNT(DISTINCT order_id) FILTER (WHERE action = 'deliver_order') AS deliver_order

FROM courier_actions
    WHERE DATE_PART('month', time) = 9

GROUP BY 
    courier_id

HAVING 
    COUNT(DISTINCT order_id) FILTER (WHERE action = 'deliver_order') = 1

ORDER BY 
    deliver_order DESC