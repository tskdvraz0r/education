/* Задача 6:
С помощью функции AGE() и агрегирующей функции снова рассчитайте возраст самого молодого курьера мужского пола в таблице couriers, 
но в этот раз в качестве первой даты используйте последнюю дату из таблицы courier_actions. Чтобы получилась именно дата, перед 
применением функции AGE() переведите посчитанную последнюю дату в формат DATE, как мы делали в этом задании. Возраст курьера измерьте 
количеством лет, месяцев и дней и переведите его в тип VARCHAR. Полученную колонку со значением возраста назовите min_age.

Поле в результирующей таблице: 
min_age */

WITH last_date_count AS 
(
    SELECT 
        MAX(time)::DATE AS last_date
    
    FROM courier_actions
)


SELECT
    MIN(
        AGE(
            (SELECT
                last_date
            
            FROM last_date_count), birth_date)::VARCHAR) AS min_age

FROM couriers
    WHERE sex = 'male'
        AND birth_date IS NOT NULL