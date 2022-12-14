-- Active: 1671137145177@@127.0.0.1@3306@interactive_sql
/* Вычислить среднюю цену и суммарную стоимость тех книг, количество экземпляров которых принадлежит интервалу от 5 до 14, включительно.
Столбцы назвать Средняя_цена и Стоимость, значения округлить до 2-х знаков после запятой. */

--16.12.2022
SELECT
    ROUND(AVG(price), 2) AS 'Средняя_цена',
    ROUND(SUM(amount * price), 2) AS 'Стоимость'

FROM book
    WHERE amount BETWEEN 5 AND 14