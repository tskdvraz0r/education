/* Задача 6:
    Посчитайте количество заказов в таблице orders с девятью и более товарами. Для этого воспользуйтесь функцией array_length, 
отфильтруйте данные по количеству товаров в заказе и проведите агрегацию. Полученный столбец назовите orders_count.
    Поле в результирующей таблице: orders_count */

SELECT
    COUNT(order_id) AS orders_count

FROM orders
    WHERE ARRAY_LENGTH(product_ids, 1) > 8