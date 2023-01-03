/* Задача 10:
Из таблицы user_actions отберите пользователей, у которых последний заказ был создан до 1 сентября 2022 года. 
Выведите только их id, дату создания заказа выводить не нужно. Результат отсортируйте по возрастанию id пользователя.

Поле в результирующей таблице:
user_id */

SELECT
    DISTINCT user_id

FROM user_actions
    WHERE action = 'create_order'
    
GROUP BY 
    user_id

HAVING 
    DATE_PART('month', MAX(time)) < 9
    
ORDER BY 
    user_id