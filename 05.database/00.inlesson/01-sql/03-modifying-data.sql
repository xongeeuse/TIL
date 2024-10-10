-- Active: 1728538407910@@127.0.0.1@3306
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content TEXT NOT NULL,
  created_at DATE NOT NULL
);



-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table
INSERT INTO articles (title, content, created_at)
  VALUES 
    ('제목 1', '내용 1', '2000-01-01'),
    ('제목 2', '내용 2', '2001-01-01'),
    ('제목 3', '내용 3', '2002-01-01');

-- 2. Update data in table
Update
  articles
SET
  title = 'UPDATE TITLE',
  content = 'UPDATE CONTENT'
WHERE
  id = 2;

-- 3. Delete data from table
DELETE FROM articles
WHERE
  id = 1;