-- orders 테이블 삭제
DROP TABLE orders;

-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블, customers 테이블과 관계 형성
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    customer_id INTEGER,            -- 고객 ID (외래 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    price INTEGER,                  -- 주문 가격 (정수 타입)
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)  -- customers 테이블과 관계 형성
);

-- orders 테이블에 price 컬럼 추가
ALTER TABLE orders ADD COLUMN price INTEGER;

-- orders 테이블에서 total_amount 컬럼 삭제
ALTER TABLE orders DROP COLUMN total_amount;

-- orders 테이블에 데이터 삽입
INSERT INTO orders (order_id, customer_id, order_date, price) VALUES
    (1, 1, '2023-07-15', 50),     -- 2023년 7월 15일 주문, 가격: 50, 고객 ID: 1
    (2, 2, '2023-07-16', 75),     -- 2023년 7월 16일 주문, 가격: 75, 고객 ID: 2
    (3, 3, '2023-07-17', 30);     -- 2023년 7월 17일 주문, 가격: 30, 고객 ID: 3

-- orders 테이블과 customers 테이블을 조인하여 주문 정보와 고객 이름을 함께 조회
SELECT orders.order_id, customers.name, orders.order_date, orders.price
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;