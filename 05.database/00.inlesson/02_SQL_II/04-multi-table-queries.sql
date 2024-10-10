-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  -- userId 컬럼은 외래키로 지정할 거야.
  -- 외래키로 지정시 반드시 필수적으로 따라붙는 옵션
  FOREIGN KEY (userId) 
    -- usrId 외래키는 users 테이블의 id 컬럼을 참조한다.
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
SELECT * FROM articles
INNER JOIN users
  ON users.id = articles.userId;

-- 하석주가 작성한 게시글 모두 조회
SELECT * FROM articles
INNER JOIN users
  ON users.id = articles.userId
WHERE users.name = '하석주';

-- LEFT JOIN
-- 왼쪽 테이블의 모든 레코드와 ON 에 일치하는 오른쪽 테이블
SELECT * FROM articles
LEFT JOIN users
  ON users.id = articles.userId;

SELECT * FROM users
LEFT JOIN articles
  ON users.id = articles.userId;

SELECT * FROM articles
RIGHT JOIN users
  ON users.id = articles.userId;