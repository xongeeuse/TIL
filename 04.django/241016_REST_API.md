# REST API_1

## REST API
### API
- 두 소프트웨어가 서로 통신할 수 있게 하는 매커니즘
- 클라이언트-서버 처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

### REST
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- REST 원리를 따르는 시스템을 RESTful하다고 함
- *자원을 정의하고 자원에 대한 주소를 지정*하는 전반적인 방법 서술
- 각각 API 서버 구조를 작성하는 모습이 너무 다르니 어느정도 약속을 만들어서 다같이 통일해서 쓰자!

#### REST에서 자원을 정의하고 주소를 지정하는 방법
1. 자원의 식별
  - URI(Uniform Resource Identifier, 통합 자원 식별자)
    - 인터넷에서 리소스(자원)를 식별하는 문자열
    - 가장 일반적인 URI는 웹 주소로 알려진 URL
    - URL(통합 자원 위치): 웹에서 주어진 리소스의 주소

2. 자원의 행위
  - HTTP Methods
3. 자원의 표현
  - JSON 데이터(궁극적으로 표현되는 데이터 결과물)


### DRF
- Django REST Framework: Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

#### Serialization, 직렬화
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
