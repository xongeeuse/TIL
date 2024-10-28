# 📌241028 Controlling Event

## 이벤트

- 웹에서의 모든 동작은 이벤트 발생과 함께!
- 무언가 일어났다는 신호, 사건
- 모든 DOM 요소는 이러한 event를 만들어 냄

### `event` object(이벤트 객체)

- DOM에서 이벤트가 발생했을 때 생성되는 객체
- 이벤트 종류
  - mouse, input, keyboard, touch...
  - DOM 요소에서 event가 발생하면, 해당 event는 연결된 이벤트 처리기(event handler)에 의해 처리됨

### event handler

- 특정 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

- `.addEventListener()`

  - 대표적인 이벤트 핸들러 중 하나
  - 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
  - EventTarget.addEventListener(type, handler)

    - "대상에 특정 Event가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다"
    - `EventTarget`: DOM 요소
    - `type`
      - 수신할 이벤트 이름
      - 문자열로 작성(ex. 'click')
    - `handler`
      - 발생한 이벤트 객체를 수신하는 콜백 함수
      - 이벤트 핸들러는 자동으로 event 객체를 매개변수로 받음

    ```JavaScript
    element.addEventListener('click', function (event) {
        // 이벤트 처리 로직
    })
    ```

#### addEventListener의 콜백 함수 특징

- 이벤트 핸들러 내부의 this는 이벤트 리스너에 연결된 요소(currentTarget)을 가리킴
- 이벤트가 발생하면 event 객체가 생성되어 첫번째 인자로 전달
- event 객체가 필요 없는 경우 생략 가능
- 반환 값 없음

## 버블링

- "한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상"
- 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작
- 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물 속 거품과 닮았기 때문
- 최하위의 <p>요소를 클릭하면 p -> div -> form 순서로 3개의 이벤트 핸들러가 모두 순차적으로 동작했던 것

### 이벤트가 정확히 어디서 발행했는지 접근할 수 있는 방법

- `currentTarget`
  - '현재' 요소
  - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  - `this`와 같음
- `target`
  - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
  - 실제 이벤트가 시작된 요소
  - 버블링이 진행되어도 변하지 않음

### 캡처링

- table의 하위 요소 td를 클릭하면 이벤트는 먼저 최상위 요소부터 아래로 전파됨(캡처링)
- 실제 이벤트가 발생한 지점(event.target)에서 실행된 후 다시 위로 전파(버블링)
  - 이 전파 과정에서 상위 요소에 할당된 이벤트 핸들러들이 호출되는 것
- 캡처링은 실제 개발자가 다루는 경우가 거의 없으므로 버블링에 집중하기

### `currentTarget` 주의사항

- console.log()로 event 객체를 출력할 경우, currentTarget 키의 값은 null을 가짐
- currentTarget은 이벤트가 처리되는 동안에만 사용할 수 있기 때문
- 대신 console.log(event.currentTarget)을 사용하여 콘솔에서 확인 가능
- currentTarget 이후의 속성 값들은 _'target'을 참고해서 사용하기_

### 이벤트의 기본 동작 취소하기

- HTML의 각 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해가 되는 경우가 있어 이벤트의 기본 동작을 취소할 필요가 있음
- ex.
  - form 요소의 제출 이벤트를 취소하여 페이지 새로고침을 막을 수 있음
  - a 요소를 클릭할 때 페이지 이동을 막고 추가 로직을 수행할 수 있음
- `.preventDefault()`: 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정
  > 교재 p.54-64 파일 참고해서 다시 해보기!
  > addEventListener와 화살표 함수 주의사항 다시 보기!
