# 240925_Django Form

## HTML 'form'
- 지금까지 사용자로부터 데이터를 제출받기 위해 활용한 방법
- 그러나 비정상적 or 악의적인 요청을 필터링할 수 없음
- 유효한 데이터인지에 대한 확인이 필요 => 유효성 검사

### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 구현을 위해서는 입력 값, 형식, 중복, 범위, 보안 등 고려사항 많음
- 직접 개발 X, Django가 제공하는 Form을 사용

#### is_valid()
- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환
- 별도로 명시하지 않았지만, 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정되어 있음
- 빈 값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨

### Form Class
#### Django Form
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화할 수 있는 기능 제공

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때
  - ex. 게시글 작성, 회원가입
- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때
  - Model과 연결된 Form을 자동으로 생성해주는 기능 제공 (Form + Model)
  - 게시글 작성, 회원가입
  - `Meta` class
    - ModelForm의 추가 정보나 속성을 작성하는 곳
    - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
    - 파이썬의 inner class와 같은 문법적 관점으로 접근하지 말 것

- save() 메서드가 생성과 수정을 구분하는 법
- 키워드 인자 instance 여부를 통해 생성(create)할지 수정(update)할지 결정