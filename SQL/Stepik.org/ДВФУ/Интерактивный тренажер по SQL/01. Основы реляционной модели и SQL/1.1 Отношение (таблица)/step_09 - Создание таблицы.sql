-- Active: 1671137145177@@127.0.0.1@3306@interactive_sql
/* Сформулируйте SQL запрос для создания таблицы book, занесите  его в окно кода (расположено ниже) и отправьте на проверку (кнопка Отправить). Структура таблицы book:

+---------+--------------------------------+
| Поле	  | Тип, описание                  |
+---------+--------------------------------+
| book_id | INT PRIMARY KEY AUTO_INCREMENT |
| title	  | VARCHAR(50)                    |
| author  |	VARCHAR(30)                    |
| price	  | DECIMAL(8, 2)                  |
| amount  |	INT                            |
+---------+--------------------------------|
*/

-- 16.12.2022
CREATE TABLE book
(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT
);