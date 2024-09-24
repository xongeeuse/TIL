# 240924_ORM

##
- variable routing: 주소 일부를 변수로 받아서 구성

## HTTP
- 네트워크 상에서 데이터(리소스)를 주고 받기 위한 약속

### HTTP request methods
- 데이터에 대해 수행을 원하는 작업(행동)을 나타내는 것
  - 서버에게 원하는 작업의 종류를 알려주는 역할
- 클라이언트가 웹 서버에 특정 동작을 요청하기 위해 사용하는 표준 명령어
- 대표 메서드 `GET`, `POST`

1. `GET` Method
- 서버로부터 데이터를 요청하고 받아오는데(조회) 사용
- 특징
  - **데이터 전송**
    - URL의 *쿼리 문자열(Query String)*을 통해 데이터를 전송
    - http://127.0.0.1:8000/articles/create/?*title=제목&content=내용*
  - **데이터 제한**
    - URL 길이에 제한이 있어 대량의 데이터 전송에 적합하지 않음
  - **브라우저 히스토리**
    - 요청 URL이 브라우저 히스토리에 남음
  - **캐싱**
    - 브라우저는 GET요청의 응답을 로컬에 저장할 수 있음
    - 동일한 URL로 다시 요청할 때, 서버에 접속하지 않고 저장된 결과를 사용
    - 페이지 로딩 시간을 크게 단축
- 언제 쓰나요?
  - 검색 쿼리 전송
  - 웹페이지 요청
  - API에서 데이터 조회

2. `POST` Method
- 서버에 데이터를 제출하여 리소스를 변경(생성, 수정, 삭제)하는데 사용
- 특징
  - 데이터 전송
    - HTTP Body를 통해 데이터를 전송
  - 데이터 제한
    - GET에 비해 더 많은 양의 데이터를 전송할 수 있음
  - 브라우저 히스토리
    - POST 요청은 브라우저 히스토리에 남지 않음
  - 캐싱
    - POST 요청은 기본적으로 캐시할 수 없음
    - POST 요청이 일반적으로 서버의 상태를 변경하는 작업을 수행하기 때문
- 언제 쓰나요?
  - 로그인 정보 제출
  - 파일 업로드
  - 새 데이터 생성(ex. 새 게시글 작성)
  - API에서 데이터 변경 요청

  3. `GET` `POST` 정리
    - GET과 POST는 각 특성에 맞게 적절히 사용해야 함
    - `GET`: 데이터 조회
    - `POST`: 데이터 생성이나 수정에 주로 사용


### CSRF(Cross-Site-Request-Forgery)
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- CSRL Token 적용
  - `{% csrf_token %}`
  - DTL의 `csrf_token`태그를 사용해 손쉽게 사용자에게 토큰 값 부여
  - 요청 시 토큰 값도 함께 서버로 전송될 수 있도록 함

- 왜 `POST`일 때만 Token을 확인할까?
  - POST는 단순 조회를 위한 GET과 달리 *특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 의미와 기술적인 부분*을 가지고 있기 때문
  - DB에 조작을 가하는 요청은 반드시 인증 수단이 필요
  - 데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것


  ### Redirect
  - 게시글 작성 후 작성완료 페이지를 띄우는 것은 아주 부자연스러운 흐름
  - 서버는 데이터 저장 후 페이지를 응답하는 것이 아닌 사용자를 적절한 기존 페이지로 보내야한다.
  - 사용자를 보낸다 => 사용자가 GET요청을 한번 더 보내도록 해야 한다.
  - 실제로 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아닌 클라이언트가 GET 요청을 한번 더 보내도록 응답하는 것

  #### redirect() 함수 적용
  - `create` view 함수 변경
  ```python
  from django.shortcuts import render, redirect

  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
      article = Article(title=title, content=content)
      article.save()
      return redirect('articles:detail', article.pk)
  ```

  #### redirect 동작 원리(클라이언트 <=> 장고)
  1. client => : [POST] 게시글 작성 요청(+입력 데이터)
  2. django : `create` view 함수 호출
  3. <= django : redirect 응답(detail 주소로 요청을 보내라)
  4. client => : [GET] detail 페이지 요청
  5. django : `detail` view 함수 호출
  6. <= django : detail 페이지 응답


  ### Update
  