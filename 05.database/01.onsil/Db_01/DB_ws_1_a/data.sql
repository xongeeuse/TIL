-- Active: 1728538407910@@127.0.0.1@3306

CREATE TABLE songs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  album TEXT NOT NULL,
  genre TEXT NOT NULL,
  duration INTEGER
);

PRAGMA table_info('songs');

-- 데이터 삽입 5개 이상
INSERT INTO songs(title, artist, album, genre, duration)
VALUES
  ('제목 1', '가수 1', '앨범 1', 'Pop', 200),
  ('제목 2', '가수 2', '앨범 2', 'Rock', 300),
  ('제목 3', '가수 3', '앨범 3', 'Hip Hop', 250),
  ('제목 4', '가수 4', '앨범 4', 'Electronic', 180),
  ('제목 5', '가수 5', '앨범 5', 'R&B', 320);

SELECT * FROM songs;

UPDATE
  songs
SET
  title = '수정 제목'
WHERE
  id = 2;