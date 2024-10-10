-- Active: 1728545317640@@127.0.0.1@3306

SELECT
  genre, COUNT(*)
FROM
  songs
GROUP BY
  genre;

SELECT
  genre, COUNT(*),
  AVG(duration) AS 'average_duration'
FROM
  songs
GROUP BY
  genre;
