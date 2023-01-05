/* Задача :
------------------------------------------------------------------------------------------------------------------------------------------------------
    Из таблицы orders выведите id и содержимое заказов, которые включают хотя бы один из пяти самых дорогих товаров, доступных в нашем сервисе. 
Результат отсортируйте по возрастанию id заказа.

Поля в результирующей таблице: 
order_id, product_ids */

WITH most_expensive_products AS
(
    SELECT
        product_id
        
    FROM products
    
    ORDER BY
        price DESC
    
    LIMIT 5
),

flat_table AS
(
    SELECT
        order_id,
        UNNEST(product_ids) AS product_id
    
    FROM orders
),

most_exp_in_order AS
(
    SELECT
        order_id,
        CASE
            WHEN product_id IN (
                                    SELECT
                                        product_id
                                    
                                    FROM most_expensive_products
                                    
                                ) THEN 'yes'
            
            ELSE 'no'
        END AS cont_most_exp
    
    FROM flat_table
)

SELECT
    order_id,
    product_ids

FROM orders
    WHERE order_id IN ( SELECT
                            DISTINCT order_id
                        
                        FROM most_exp_in_order
                            WHERE cont_most_exp = 'yes')

ORDER BY
    order_id ASC