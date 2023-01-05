/* Задача 8:
Используя данные из таблицы user_actions, рассчитайте, сколько заказов сделал каждый пользователь и отразите это в столбце orders_count. 
В отдельном столбце orders_avg напротив каждого пользователя укажите среднее число заказов всех пользователей, округлив его до двух знаков после запятой. 
Также для каждого пользователя посчитайте отклонение числа заказов от среднего значения. Отклонение считайте так: число заказов «минус» округлённое среднее значение. 
Колонку с отклонением назовите orders_diff. Результат отсортируйте по возрастанию id пользователя.

Поля в результирующей таблице:
 user_id, orders_count, orders_avg, orders_diff */

WITH subquery AS
(
    SELECT
        user_id, 
        COUNT(DISTINCT order_id) AS orders_count
    
    FROM user_actions

    GROUP BY
        user_id
)

SELECT
    user_id, 
    orders_count,
    ROUND((
            SELECT 
                AVG(orders_count)
            
            FROM subquery), 2) AS orders_avg,
            
    (orders_count - ROUND((
                            SELECT
                                AVG(orders_count)
                            
                            FROM subquery), 2)) AS orders_diff

FROM subquery
ORDER BY
    user_id ASC