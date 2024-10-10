-- Active: 1728547029896@@127.0.0.1@3306

SELECT
  *
FROM
  users
WHERE
  age >= 30
  AND balance >= 1000;

SELECT
  *
FROM
  users
WHERE
  balance <= 1000
  AND age <= 20;

SELECT
  *
FROM
  users
WHERE
  first_name LIKE '현%'
  AND country = '제주특별자치도'
ORDER BY
  age DESC
limit 1;

SELECT
  *
FROM
  users
WHERE
  first_name = '재은'
  OR first_name = '영일'
ORDER BY
  balance DESC
LIMIT 1;

SELECT
  *
FROM
  users
GROUP BY
  country
HAVING
  MAX(balance)
ORDER BY
  balance DESC;

SELECT
  *
FROM
  users
WHERE
  age >= 30
  AND balance > (
    SELECT
      AVG(balance)
    FROM
      users
    WHERE
      age >= 30);