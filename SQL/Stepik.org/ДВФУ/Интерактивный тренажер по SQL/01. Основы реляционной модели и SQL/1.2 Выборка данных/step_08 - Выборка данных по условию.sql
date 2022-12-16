-- Active: 1671137145177@@127.0.0.1@3306@interactive_sql
/* Вывести автора, название  и цены тех книг, количество которых меньше 10. */

--16.12.2022
SELECT
    author,
    title,
    price

FROM book
    WHERE amount < 10 