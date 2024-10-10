-- Active: 1728528371968@@127.0.0.1@3306

-- tracks 테이블의 모든 데이터 조회
SELECT
  *
FROM
  tracks;

-- Name, Milliseconds, UnitPrice 열의 모든 데이터 조회
SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;

-- GenreID 값이 1인 모든 데이터 조회
SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1;

-- 모든 데이터를 name 기준 오름차순 정렬 조회
SELECT
  *
FROM
  tracks
ORDER BY
  Name;

-- tracks 테이블의 모든 데이터 조회, 10개만 출력
SELECT
  *
FROM
  tracks
limit
  10;