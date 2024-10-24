# 📌241023 Reference Type 1

## 객체, Object

- 키로 구분된 데이터 집합을 저장하는 자료형

### 객체 구조

- 중괄호 `{}`를 이용해 작성
- 중괄호 안에는 `key: value`쌍으로 구성된 속성을 여러 개 작성 가능
- key는 문자형만 허용 (문자열에 공백 없으면 따옴표 생략 가능)
- value는 모든 자료형 허용

### 속성 참조

- `.` 또는 `[]`로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

### `in` 연산자

- 속성이 객체에 존재하는지 여부를 확인

### 메서드

- Method, _객체 속성에 정의된 함수_
- `object.method()` 방식으로 호출
- 메서드는 객체를 행동할 수 있게 함
- `this` 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음
  - `this` keyword
    - 함수나 메서드를 호출한 객체를 가리키는 키워드
    - 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
    - JavaScript에서 this는 함수를 호출하는 방법에 따라 가리키는 대상이 다름
      - 단순 호출: 전역 객체(window? JavaScript에서 최상위 객체)
      - 메서드 호출: 메서드를 호출한 객체
- 중첩된 함수에서의 this 문제점과 해결책
- > 중첩된 함수에서의 this가 이런 상황에서 문제 발생하기 때문에 콜백함수를 화살표 함수로 선언해줘야 함

  - forEach의 인자로 작성된 함수는 일반적인 함수 호출이기 때문에 this가 전역 객체를 가리킴

    ```javascript
    const myObj2 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.numbers.forEach(function (number) {
          console.log(this); // window
        });
      },
    };

    console.log(myObj2.myFunc());
    ```

  - 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수(myFunc)에서의 this 값을 가져옴

    ```javascript
    const myObj3 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.numbers.forEach((number) => {
          console.log(this); // window
        });
      },
    };

    console.log(myObj3.myFunc());
    ```

#### `this`

- JavaScript 함수는 호출될 때 this를 암묵적으로 전달 받음
- JavaScript에서 this는 함수가 호출되는 방식에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해
- JavaScript의 this는 *함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정*됨(동적 할당)
  - 장점: 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
  - 단점: 이런 유연함이 실수로 이어질 수 있다는 것
  - 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데 집중


### Optional Chaining(`?.`)
- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 대신 평가를 멈추고 undefined를 반환
- 물음표 왼쪽의 대상 확인하는 거!
- 만약 Optional Chaining을 사용하지 않는다면, `&&`연산자 사용해야 함
- 장점
  - 참조가 누락될 가능성이 있는 경우, 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음
  - 어떤 속성이 필요한지에 대한 보증이 확실하지 않은 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음
- 주의사항
  - 존재하지 않아도 괜찮은 대상에만 사용해야 함(남용 X)
    - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용
    - 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문
  - Optional Chaining 앞의 변수는 반듣시 선언되어 있어야 함