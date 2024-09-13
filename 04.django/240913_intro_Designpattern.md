# 240913_Intro & Design Pattern

## django
- `python` 기반의 대표적인 웹 프레임워크

### django를 사용해서 서버를 구현하려면?
#### 가상환경
- `python` 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 *독립적인* 실행 환경
  - 프로젝트 A와 B 진행 시 2가지 버전의 패키지를 사용해야 하는 경우,
  - 파이썬 환경에서는 1개의 버전만 존재할 수 있기 때문에
  - 각 프로젝트의 독립적인 개발 환경 필요!

- `venv`라는 이름의 가상환경 생성
  - `python -m venv venv`
  - 뒤에 오는 `venv`는 가상환경의 이름. 임의 설정 가능하지만 관례적으로 venv 사용
- 가상환경을 생성했다면 on/off 를 통해 이용할 수 있음(in/out 개념 아님!)
  - `source venv/Scripts/activate`
  - `(venv)`가 보인다면 가상환경 on-
  - 해당 폴더가 아니더라도 경로를 따라가서 가상환경 on/off 가능
- 설치된 패키지 목록 생성
- `pip freeze > requirements.txt`
  - `requirements.txt` 파일에 pip list 저장됨
  - 각자 다른 가상 환경에서 프로젝트를 진행하다가 협업을 하는 경우,
  - 해당 프로젝트를 위해 *어떤 패키지를 설치했고, 어떤 버전을 설치했는지* 패키지 목록 공유
  - venv 자체를 직접 공유하기엔 비효율적 => pip list 공유
  - `pip install -r requirements.txt`
    - 생성된 list 기반으로 패키지 설치해 동일한 환경 구성
- `deactivate`: 가상환경 비활성화 명령어
  
#### django 프로젝트 생성 및 실행
- `django-admin startproject firstpjt .`: `firstpjt`라는 이름의 프로젝트 생성
- `python manage.py runserver`: django 서버 실행

### MVC 디자인 패턴
- Model, Design, Controller
- 애플리케이션을 구조화하는 대표적인 패턴
- 데이터 & 사용자 인터페이스 & 비즈니스 로직을 분리
- 시각적 요소와 뒤에서 실행되는 로직을 서로 영향없이 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해

### MTV 디자인 패턴
- Model, Template, View
- django에서 애플리케이션을 구조화하는 패턴
- 기존 MVC 패턴과 동일하나, 단순히 명칭을 다르게 정의한 것

### 프로젝트와 앱
- 프로젝트: 애플리케이션의 집합
- 애플리케이션: 독립적으로 작동하는 기능 단위 모듈
  - 반드시 ***앱을 생성한 후 등록***해야 함! (등록 후 생성은 불가능)
  



# E-book 참고 파트 다시 보기~~~~~~~~~!