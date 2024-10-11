-- Active: 1728548875889@@127.0.0.1@3306

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_data DATE NOT NULL,
  total_amount REAL NOT NULL
);

PRAGMA table_info('orders');

INSERT INTO orders (order_data, total_amount)
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25);

SELECT * FROM orders;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);

PRAGMA table_info('customers');

INSERT INTO customers (name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('허균', 'lee.cheolsu@example.com', '010-5555-4444');

SELECT * FROM customers;

DELETE FROM orders
WHERE
  order_id = 3;

UPDATE 
  customers
SET
  name = '홍길동'
WHERE
  customer_id = 1;

SELECT * FROM orders;
SELECT * FROM customers;