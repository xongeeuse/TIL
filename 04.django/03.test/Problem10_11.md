### 문제 10. (서술형) Django의 Form과 ModelForm의 차이점을 설명하고, 각각 어떤 상황에서 사용하는 것이 적절한지 서술하시오.
- Form은 데이터의 조회만 필요할 때, ModelForm은 데이터의 생성, 수정 및 삭제가 필요할 때 사용한다.


### 문제 11. (서술형) Django의 MTV 패턴을 기반하여 HTTP 요청 응답이 반환되기까지의 흐름을 서술하시오.
- Model, Template, View
- Model을 생성해 DB에 등록하면, 그를 기반으로 데이터를 받아올 수 있다.
- View 함수 실행해 요청 수행하고 적절한 응답 화면(Template)으로 연결하고,
- Template은 사용자에게 화면 반환한다.

