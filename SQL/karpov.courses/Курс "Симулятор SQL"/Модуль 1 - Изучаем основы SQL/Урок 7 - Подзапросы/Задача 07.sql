/* Задача 7:
Из таблицы user_actions с помощью подзапроса или табличного выражения отберите все заказы, которые не были отменены пользователями. 
Выведите колонку с id этих заказов. Результат запроса отсортируйте по возрастанию id заказа.

Поле в результирующей таблице: 
order_id */

WITH lst_cncl_ordrs AS
(
    SELECT
        DISTINCT order_id AS canceled_orders
        
    FROM user_actions
        WHERE action = 'cancel_order'
)


SELECT 
    order_id

FROM user_actions
    WHERE order_id NOT IN ( SELECT
                                canceled_orders
                            
                            FROM lst_cncl_ordrs)

ORDER BY 
    order_id ASC