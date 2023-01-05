/* Задача 15:
------------------------------------------------------------------------------------------------------------------------------------------------------
    Посчитайте возраст каждого пользователя в таблице users. Возраст измерьте числом полных лет, как мы делали в прошлых уроках. Возраст считайте 
относительно последней даты в таблице user_actions. В результат включите колонки с id пользователя и возрастом. Для тех пользователей, у которых в 
таблице users не указана дата рождения, укажите среднее значение возраста всех остальных пользователей, округлённое до целого числа. Колонку с 
возрастом назовите age. Результат отсортируйте по возрастанию id пользователя.

Поля в результирующей таблице: 
user_id, age */

-- last_date
WITH tb_last_date AS
(
    SELECT
        MAX(time) AS last_date
    
    FROM user_actions
),

-- users_age
tb_users_age AS
(
    SELECT
    user_id,
    DATE_PART('year', AGE(( 
                            SELECT
                                last_date
                                
                            FROM tb_last_date
                            ), birth_date)) AS user_age,
    sex

    FROM users
),

-- avg_users_age
tb_avg_users_age AS
(
    SELECT
        AVG(user_age) AS avg_user_age
        
    FROM tb_users_age
        WHERE user_age IS NOT NULL
)

-- null_to_avg_age
SELECT
    user_id,
    CASE
        WHEN user_age IS NULL THEN ( 
                                SELECT
                                    avg_user_age
                                
                                FROM tb_avg_users_age
                                )
        
        ELSE user_age
    END AS age

FROM tb_users_age

ORDER BY 
    user_id ASC