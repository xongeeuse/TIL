-- Active: 1728528763896@@127.0.0.1@3306

-- Name에 love 포함한 데이터 조회
SELECT
  *
FROM
  tracks
WHERE
  Name LIKE '%love%';

-- GenreID 값이 1이고, Milliseconds가 300000 이상인 데이터 모두 조회하여
SELECT
  *
FROM
  tracks
WHERE
  GenreID = 1
  AND Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;

SELECT
  GenreId, COUNT(*) AS 'TotalTracks'
FROM
  tracks
GROUP BY
  GenreId;

SELECT
  GenreId,
  SUM(UnitPrice) AS 'TotalPrice'
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;