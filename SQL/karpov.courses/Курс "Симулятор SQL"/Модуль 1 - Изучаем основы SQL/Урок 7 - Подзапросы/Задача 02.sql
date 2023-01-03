/* Задача 2:
Повторите запрос из предыдущего задания, но теперь вместо подзапроса используйте оператор WITH и табличное выражение. Условия задачи те же.

Поле в результирующей таблице: 
orders_avg */

WITH subquery_1 AS
(
    SELECT
        user_id,
        COUNT(DISTINCT order_id) FILTER (WHERE action != 'cancel_order') AS user_orders
    
    FROM user_actions
    
    GROUP BY 
        user_id
)


SELECT 
    ROUND(AVG(user_orders), 2) AS orders_avg
    
FROM subquery_1