# django 시작하기

```bash
# 1. 프로젝트 시작하자마자 gitignore 생성하기
$ code .gitignore

# 2. 가상 환경 생성하기
$ python -m venv venv

# 3. 가상환경 활성화 하기
$ source venv/Scripts/Activate

# 4. 프로젝트 진행에 필요한 라이브러리 설치하기
$ pip install django

# 5. 현재 버젼을 다음에도 똑같이 유지하기위해 기록
$ pip freeze > requirements.txt
```

> 우리는 파이썬 버젼 3.9.x 쓰고있습니다.
> `pip install django` 명령어 실행
> 설치되는 장고 버전은 4.2.x 버전입니다.

> 그런데...
> 최신 버전 파이썬은? 3.1x.x 입니다.
> 그상태에서 위 명령어 실행시 django 5.1.x 설치됩니다.

---

2. django 프로젝트 생성하기
```bash
# 장고야 프로젝트시작해줘 my_pjt를 현재폴더에.
$ django-admin startproject my_pjt .

# 1. 서버 키기
$ python manage.py runserver

# 2. 서버 끄기
ctrl + c
```
---

3. 앱 생성 및 등록
```bash
# 가능하지만 안씀
# $ django-admin startapp my_app

# 1. 앱 생성 -> 등록
$ python manage.py startapp my_app

```

> 프로젝트는 프로젝트 생성 명령어로 만듬
  - 이때, app은 없었음.
> 그리고나서, 추가로 app을 생성했음.
  - 이건.. 프로젝트랑 완전 별개 폴더(패키지)이다.
> 프로젝트가 방금 만들어진 app의 존재를 알 리가 없다.


