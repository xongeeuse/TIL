-- Active: 1728549812194@@127.0.0.1@3306
-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    total_amount REAL               -- 총 주문 금액 (실수 타입)
);

-- orders 테이블에 데이터 삽입
INSERT INTO orders (order_id, order_date, total_amount) VALUES
    (1, '2023-07-15', 50.99),      -- 2023년 7월 15일 주문, 총 주문 금액: 50.99
    (2, '2023-07-16', 75.50),      -- 2023년 7월 16일 주문, 총 주문 금액: 75.50
    (3, '2023-07-17', 30.25);      -- 2023년 7월 17일 주문, 총 주문 금액: 30.25

-- customers 테이블 생성: 고객 정보를 저장하기 위한 테이블
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, -- 고객 ID (기본 키)
    name TEXT,                      -- 고객 이름 (텍스트 타입)
    email TEXT,                     -- 고객 이메일 (텍스트 타입)
    phone TEXT                      -- 고객 전화번호 (텍스트 타입)
);

-- customers 테이블에 데이터 삽입
INSERT INTO customers (name, email, phone) VALUES
    ('허균', 'hong.gildong@example.com', '010-1234-5678'),    -- 허균 고객 정보
    ('김영희', 'kim.younghee@example.com', '010-9876-5432'),  -- 김영희 고객 정보
    ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');    -- 이철수 고객 정보

-- orders 테이블에서 order_id가 3인 주문 정보 삭제
DELETE FROM orders WHERE order_id = 3;

-- customers 테이블에서 customer_id가 1인 고객의 이름을 '홍길동'으로 수정
UPDATE customers SET name = '홍길동' WHERE customer_id = 1;

-- orders 테이블의 모든 데이터 조회
SELECT * FROM orders;

-- customers 테이블의 모든 데이터 조회
SELECT * FROM customers;



-- my SOL
-- orders 테이블 삭제
DROP TABLE orders;

-- orders 새로 생성
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,   -- 주문 ID (기본 키)
    order_date DATE NOT NULL,                -- 주문 날짜 (날짜 타입)
    total_amount REAL NOT NULL,               -- 총 주문 금액 (실수 타입)
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

ALTER TABLE
    orders
ADD COLUMN
    price INTEGER NOT NULL;

ALTER TABLE
    orders
DROP COLUMN
    total_amount;

PRAGMA table_info('orders');

INSERT INTO orders (order_date, customer_id, price)
VALUES
    ('2023-07-15', 1, 50),
    ('2023-07-16', 2, 75),
    ('2023-07-17', 3, 30);

SELECT * FROM orders;

-- SELECT
--     *
-- FROM
--     orders
-- JOIN customers
--     ON customers.customer_id = orders.customer_id;

SELECT
    o.order_id, c.name, o.order_date, o.price
FROM
    orders o, customers c
WHERE
    