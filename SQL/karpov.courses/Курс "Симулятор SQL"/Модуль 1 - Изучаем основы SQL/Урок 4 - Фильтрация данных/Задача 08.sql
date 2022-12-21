/* Задание 8:
Определите id и дату рождения 50 самых молодых пользователей мужского пола из таблицы users.
Поле в результирующей таблице: user_id, birth_date

Пояснение:
Будьте внимательны и помните про NULL значения. */

SELECT
    user_id,
    birth_date
    
FROM users
    WHERE birth_date IS NOT NULL
        AND sex = 'male'
    
ORDER BY 
    birth_date desc
    
LIMIT 50