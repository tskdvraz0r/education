/* Задача 3:
Выведите из таблицы products информацию о всех товарах кроме самого дешёвого. Результат отсортируйте по убыванию id товара.

Поля в результирующей таблице: 
product_id, name, price */

WITH min_price_value AS
(
    SELECT 
        MIN(price) AS min_price
    
    FROM products
)

SELECT 
    product_id,
    name,
    price

FROM products
    WHERE price != (SELECT
                        min_price
                    
                    FROM min_price_value)

ORDER BY 
    product_id DESC 