/* Задача 4:
Выведите информацию о товарах в таблице products, цена на которые превышает среднюю цену всех товаров на 20 рублей и более. Результат отсортируйте по убыванию id товара.

Поля в результирующей таблице: 
product_id, name, price */


WITH subquery_1 AS 
(
    SELECT 
        AVG(price) + 20 AS above_avg_price
    
    FROM products
)


SELECT 
    product_id,
    name,
    price

FROM products
    WHERE price >= ( 
                    SELECT
                        above_avg_price
                    
                    FROM subquery_1
                    )

ORDER BY 
    product_id DESC