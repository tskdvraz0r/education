/* Задача 11:
Из таблицы user_actions получите информацию о всех действиях, совершённых пользователями 25 августа 2022 года с 12:00 до 15:59. Результат отсортируйте по времени совершения действия — от самых последних действий к самым первым.
Поля в результирующей таблице: user_id, order_id, action, time

Пояснение:
Для решения задачи вам могут пригодиться функции DATE и DATE_PART. Будьте аккуратны при работе со временем. */

SELECT
    user_id,
    order_id,
    action,
    time

FROM user_actions
    WHERE DATE_PART('hour', time)::VARCHAR BETWEEN '12' AND '15'
        AND time::DATE = '2022-08-25'

ORDER BY 
    time DESC