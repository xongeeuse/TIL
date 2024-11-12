#

## State Management

- Vue 컴포넌트는 이미 반응형 상태를 관리하고 있음
- 상태 === 데이터

### 컴포넌트 구조의 단순화

- 상태(State)
  - 앱 구동에 필요한 기본 데이터
- 뷰(View)
  - 상태를 선언적으로 매핑하여 시각화
- 기능(Actions)
  - 뷰에서 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작
    > "단방향 데이터 흐름"의 간단한 표현

## `Pinia`, State management library

### Pinia 구성 요소

1. `store`

   - 중앙 저장소
   - 모든 컴포넌트가 공유하는 상태, 기능 등이 작성됨
   - `defineStore()`의 반환 값의 이름은 use와 store를 사용하는 것을 권장
   - `defineStore()`의 첫번째 인자는 애플리케이션 전체에 걸쳐 사용하는 store의 고유 ID

2. `state`

   - 반응형 상태(데이터)
   - ref() === state

3. `getters`

   - 계산된 값
   - computed() === getters

4. `actions`

- 메서드
- function() === actions

> Setup Stores의 반환 값
> pinia의 상태들을 사용하려면 반드시 반환해야 함
> store에서는 공유하지 않는 private한 상태 속성을 가지지 않음
