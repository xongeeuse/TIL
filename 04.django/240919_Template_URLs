# 240919_Template_URLs

## Template System
### Django Template System
- 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
- html 콘텐츠를 변수 값에 따라 변경하기
  ```python
  # articles/vies.py

  def index(request):
    context = {
      'name': 'Jane',
    }
    return render(request, 'articles/index.html', context)
  ```
  ```html
  <!-- articles/index.html -->
  <body>
    <h1>Hello, {{ name }}</h1>
  </body>

  ```
### Django Template Language(DTL)
- Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

#### DTL Syntax
1. Variable
  - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
  - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
  - dot('.')을 사용하여 변수 속성에 접근할 수 있음
2. Filters
  - 표시할 변수를 수정할 때 사용(변수 + '|' + 필터)
  - 연결(chained)이 가능하며 일부 필터는 인자를 받기도 함
  - 약 60개의 built-in template filters 제공
3. Tags
  - 반복 또는 논리를 수행하여 제어 흐름을 만듦 `{% tag %}`
    (앞선 두 요소와 달리 출력되는 부분은 아니고! 제어 흐름만 컨트롤!)
  - 일부 태그는 시작과 종료 태그가 필요(`{% if %}`, `{% endif %}`)
  - 약 24개의 built-in template tags를 제공
4. Comments
  - DTL에서의 주석
  - 일부 키워드만 주석 처리하려면 `{# 내용 #}`
  - 영역 주석 처리하려면 `{% comment %} ... {% endcomment %}`

### 템플릿 상속(Template inheritance)
> 모든 템플릿에 bootstrap을 적용하려면? 모든 템플릿에 bootstrap CDN 작성? Nooooooooo!

- 페이지의 공통 요소를 포함하고!
- 하위 템플릿이 재정의할 수 있는 공간을 정의하는!
- 기본 skeleton 템플릿을 작성하여 상속 구조를 구축
```html
  <!-- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림 -->
  {% extends 'path' %}
  {% block content %}
    <h1>Hello, {{ name }}</h1>
  {% endblock content %}
```

### HTML form(요청과 응답)
- action
  - 입력 데이터가 전송될 URL을 지정(목적지)
  - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
- method
  - 데이터를 어떤 방식으로 보낼 것인지 정의
  - 데이터의 HTTP request methods (GET, POST)를 지정 / 검색용도로는 GET만 사용, POST는 로그인할때~
  - `input` element
    - 사용자의 데이터를 입력받을 수 있는 요소
    - 핵심 속성 `name`
      - 사용자가 입력한 데이터에 붙이는 이름(key)
      - 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근 가능
  - Query String Parameters
  
#### throw - catch 간 요청과 응답 정리
***- ebook p.53-54 순서 이해하고 정리하기!***

#### URL 이름 지정하는 부분 다시 보기!
- 모든 url에 이름 붙일거! 쌩 url 안쓸거야!
- `{% url 'app_name:path_name' %}`