# 241104_Basic_Syntax_1

## Computed Property

### `computed()`

- *계산된 속성*을 정의하는 함수
- 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 _불필요한 반복 연산을 줄임_

#### 특징

- 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음(템플릿에서는 .value 생략 가능)
- computed 속성은 의존된 반응형 데이터를 자동으로 추적
- 의존하는 데이터가 변경될 때만 재평가
  - restOfTodos의 계산은 todos에 의존하고 있음
  - 따라서 todos가 변경될 때만 restOfTodos가 업데이트됨

```javascript
const restOfTodos = computed(() => {
  return todos.value.length > 0 ? "아직 남았다" : "퇴근!";
});
```

#### `computed` vs `method`

- `computed` 속성은 의존된 반응형 데이터를 기반으로 캐시됨
- 의존하는 데이터가 변경된 경우에만 재평가됨
- 즉, 의존된 반응형 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환
- 반면, `method` 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행

##### computed와 method의 적절한 사용처

- `computed`
- _의존된 데이터가 변경되면 자동으로 업데이트_
  - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
  - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지
- `method`
- _호출해야만! 실행됨_
  - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
  - 데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수
  -

#### 캐시

- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 이후 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함

## Conditional Rendering

### HTML <template>

- 페이지가 로드될 때 렌더링되지 않지만, JS를 사용해 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 매커니즘
- 보이지 않는 wrapper 역할

### `v-if` vs `v-show`

- `v-if`
  - 초기 조건이 false인 경우 아무 작업도 수행하지 않음
  - 토글 비용이 높음
- `v-show`
  - 초기 조건에 관계 없이 항상 렌더링
  - 초기 렌더링 비용이 더 높음
- 콘텐츠를 매우 자주 전환해야 하는 경우 `v-show`,
- 실행 중 조건이 변경되지 않는 경우 `v-if` 권장

## List Rendering

### `v-for`

- 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러번 렌더링
- _반드시 `v-for`와 `key`를 함께 사용한다!_
  - 내부 컴포넌트의 상태를 일관되게 하여 데이터의 예측 가능한 행동을 유지하기 위함

#### 내장 특수 속성 `key`

- number 혹은 string으로만 사용해야 함
- key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야 함
- Vue의 내부 가상 DOM 알고리즘이 이전 목록과 새 노드 목록을 비교할 때 각 nod를 식별하는 용도로 사용

### 동일 요소에 v-for와 v-if를 함께 사용하지 않는다!

- 동일한 요소에서 v-if가 v-for보다 우선순위가 더 높기 때문
- v-if에서의 조건은 v-for범위의 변수에 접근할 수 없음
- 해결법 2가지
  - computed 활용
  - v-for와 <template> 요소 활용(05-v-for-with-v-if.html 참고)

## Watchers

### `watch()`

- 하나 이상의 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출
- watch 구조
  ```javascript
  watch(source, (newValue, oldValue) => {
    // do something
  });
  ```
  - 첫번째 인자(source)
    - watch가 감시하는 대상(반응형 변수, 값을 반환하는 함수 등)
  - 두번째 인자(callback function)
    - source가 변경될 때 호출되는 콜백 함수
    - `newValue`: 감시하는 대상이 변화된 값
    - `oldValue`(optional): 감시하는 대상의 기존 값

### computed와 watchers
- 교재 p.61 참고
- computed와  watch 모두 의존(감시)하는 원본 데이터를 직접 변경하지 않음
- 