/* Задача 2:
Отсортируйте таблицу courier_actions сначала по колонке courier_id по возрастанию id курьера, потом по колонке action (снова по возрастанию), а затем по колонке time, но уже по убыванию — от самого последнего действия к самому первому. Как вы уже догадались, сортировать таблицы можно в том числе по полям с датами и временем.
Поля в результирующей таблице: courier_id, order_id, action, time */

SELECT
    courier_id,
    order_id,
    action,
    time

FROM courier_actions

ORDER BY
    courier_id ASC,
    action ASC,
    time DESC