/* Задача 1:
------------------------------------------------------------------------------------------------------------------------------------------------------
    Объедините таблицы user_actions и users по ключу user_id. В результат включите две колонки с user_id из обеих таблиц. Эти две колонки назовите 
соответственно user_id_left и user_id_right. Также в результат включите колонки order_id, time, action, sex, birth_date. Отсортируйте получившуюся 
таблицу по возрастанию id пользователя (в любой из двух колонок с id), добавьте LIMIT 1000 в конец запроса.

Поля в результирующей таблице: 
user_id_left, 
user_id_right, 
order_id, time,
action,
sex,
birth_date */

SELECT
    ua.user_id AS user_id_left,
    u.user_id AS user_id_right,
    ua.order_id,
    ua.time,
    ua.action,
    u.sex,
    u.birth_date

FROM user_actions AS ua
    JOIN users AS u
        ON ua.user_id = u.user_id

ORDER BY
    ua.user_id ASC

LIMIT 1000