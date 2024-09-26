# 240926_Static files

## Static Files
### Static Files(정적 파일)
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- 웹 서버와 정적 파일
  - 웹 서버의 기본 동작 : 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공하는 것
  - => 이는 *자원에 접근 가능한 주소가 있다*는 의미
  - 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원을 제공함
  - ***정적 파일을 제공하기 위한 경로(URL)가 있어야 함***

### Static Files 경로
> base.html에서 load static을 한다면 자식 템플릿에서도 load static이 될까? Nooooooooooooo!

#### 기본 경로
- `app폴더/static/`까지는 기본으로 설정됨 + 이후 경로 작성
- templates 폴더와 유사
- static files 경로는 DTL의 static tag를 사용해야 함
- built-in tag가 아니기 때문에 load tag를 사용해 import 후 사용 가능
  ```html
  <!-- articles/index.html -->
  {% load static %}
  <img src="{% static "articles/sample-1.png" %}" alt="sample-image">
  ```

##### STATIC_URL
- 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
- 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재
- (웹상에 제공하기 위해 django가 만들어주는 URL)
- `URL` + `STATIC_URL` + `정적파일 경로`
  - ex. `http://127.0.0.1:8000/static/articles/sample-1.png`

#### 추가 경로
- STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
- 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
- template에서 base.html 경로에 `BASE_DIR / 'templates'` 추가하는 방식과 유사

> 정적 파일을 제공하려면 요청에 응답하기 위햔 URL이 필요!


## Media Files
### Media Files
- 사용자가 웹에서 업로드하는 정적 파일

#### ImageField()
- 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 DB에 저장되는 것이 아닌 `이미지 파일의 경로` 문자열이 저장됨
##### 미디어 파일을 제공하기 전 준비사항
1. `settings.py`에 `MEDIA_ROOT`, `MEDIA_URL` 설정
2. 작성한 `MEDIA_ROOT`와 `MEDIA_URL`에 대한 URL 지정

- MEDIA_ROOT : 미디어 파일들이 위치하는 디렉토리의 절대 경로
- MEDIA_URL : MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소 생성(STATIC_URL과 동일한 역할)


#### 이미지 파일 업로드 할 때(수정해라 나중에)
- create.html에서 새로운 데이터를 저장하는데
- form 태그는 기본적으로 텍스트 형태 데이터만 보낼 수 있도록 설정
- 파일을 보내려면 추가 설정 필요 (속성으로)
  1. `form`에서 `POST`요청 보낼 때 `enctype="multipart/form-data"`추가
  2. view 함수에서 `request.POST` 받아올 때, 두 번째 인자로 `request.FILES`추가
  > 이미지 수정하면 수정 전 파일은 필요없게 되는데 media파일은 쌓여감
더이상 참조하지 않는 파일 지우는 라이브러리 존재 => 궁금하면 검색해보기!


## 참고