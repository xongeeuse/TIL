-- Active: 1728546486976@@127.0.0.1@3306

SELECT
  AVG(age) AS 'average_age'
FROM
  users;

SELECT
  country, COUNT(*) AS 'user_count'
FROM
  users
GROUP BY
  country;

SELECT
  *
FROM
  users
ORDER BY
  balance DESC
LIMIT 1;

SELECT
  country,
  AVG(balance) AS 'avg_balance'
FROM
  users
GROUP BY
  country;

SELECT
  MAX(balance) - MIN(balance) AS 'balance_difference'
FROM
  users;