/* Задача 6:
------------------------------------------------------------------------------------------------------------------------------------------------------
    С помощью FULL JOIN объедините по ключу birth_date таблицы, полученные в результате вышеуказанных запросов (то есть объедините друг с другом два 
подзапроса). В результат включите две колонки с birth_date из обеих таблиц. Эти две колонки назовите соответственно users_birth_date и 
couriers_birth_date. Также включите в результат колонки с числом пользователей и курьеров — users_count и couriers_count. Отсортируйте получившуюся 
таблицу сначала по колонке users_birth_date по возрастанию, затем по колонке couriers_birth_date — тоже по возрастанию.

Поля в результирующей таблице: 
users_birth_date, 
users_count,  
couriers_birth_date, 
couriers_count

    После того как решите задачу, поизучайте полученную таблицу в Redash. Обратите внимание на пропущенные значения в колонках с датами рождения курьеров 
и пользователей. Подтвердилось ли наше предположение?

 */

WITH subquery_01 AS
(
    SELECT
        birth_date, 
        COUNT(user_id) AS users_count
    
    FROM users
        WHERE birth_date IS NOT NULL
    
    GROUP BY birth_date
),

subquery_02 AS
(
    SELECT
        birth_date,
        COUNT(courier_id) AS couriers_count

    FROM couriers
        WHERE birth_date IS NOT NULL

    GROUP BY birth_date
)


SELECT
    s1.birth_date AS users_birth_date,
    s1.users_count,
    s2.birth_date AS couriers_birth_date,
    s2.couriers_count

FROM subquery_01 AS s1
    FULL JOIN subquery_02 AS s2
        USING(birth_date)

ORDER BY
    users_birth_date ASC,
    couriers_birth_date ASC