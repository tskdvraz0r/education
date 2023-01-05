/* Задача 5:
    Посчитайте количество уникальных клиентов в таблице user_actions, сделавших за последнюю неделю хотя бы один заказ. 
    Полученную колонку со значением назовите users_count. В качестве текущей даты, от которой откладывать неделю, 
используйте последнюю дату в той же таблице user_actions.

Поле в результирующей таблице: 
users_count */

WITH one_week_ago AS
(
    SELECT
        MAX(time) - INTERVAL '1 week' AS day_week_ago
    
    FROM user_actions
        
)


SELECT 
    COUNT(DISTINCT user_id) FILTER (WHERE action = 'create_order') AS users_count

FROM user_actions
    WHERE time > (  SELECT 
                        day_week_ago
                    
                    FROM one_week_ago   )