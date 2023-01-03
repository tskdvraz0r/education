/* Задача 05:
    Используя функцию DATE_TRUNC, посчитайте, сколько заказов было сделано и сколько было отменено в каждом месяце. 
Расчёты проводите по таблице user_actions. Колонку с усечённой датой назовите month, колонку с количеством заказов — orders_count. 
Результат отсортируйте сначала по месяцам — по возрастанию, затем по типу действия — тоже по возрастанию.

Поля в результирующей таблице:
month, action, orders_count */

SELECT
    DATE_TRUNC('month', time)::VARCHAR AS month,
    action,
    COUNT(action) AS orders_count

FROM user_actions

GROUP BY 
    month,
    action

ORDER BY 
    month ASC,
    action ASC