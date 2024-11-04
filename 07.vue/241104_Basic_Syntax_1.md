# 241104_Basic_Syntax_1

## Template Syntax

- DOM을 기본 구성 요소 인스턴스의 데이터에 *선언적으로 바인딩*할 수 있는 HTML 기반 *템플릿 구문*을 사용

### Template Syntax의 종류

1. Text Interpolation

   - 데이터 바인딩의 가장 기본적인 형태
   - 이중 중괄호 구문을 사용
   - 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
   - msg 속성이 변경될 때마다 업데이트!

2. Raw HTML
3. Attribute Bindings
4. JavaScript Expressions

### Directive

- `v-` 접두사가 있는 특수 속성
- Directive의 속성값은 단일 JavaScript 표현식이어야 함
- (v-for, v-on 제외)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용

### Directive 전체 구문

```Vue
v-on:submit.prevent="onSubmit"
Name:Argument.Modifiers='Value'
```

1. `Arguments`
   - 일부 directive는 directive 뒤에 콜론으로 표시되는 인자를 사용할 수 있음
   - 아래 예시의 href는 HTML <a>요소의 href 속성 값을 myUrl 값에 바인딩하도록 하는 v-bind의 인자
   - 아래 예시의 click은 이벤트 수신할 이벤트 이름을 작성하는 v-on의 인자

## Dynamically data binding

### `v-bind`

- 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

#### `v-bind` 사용처

##### attribute Bindings, 속성 바인딩

- 속성 연결
- HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함
- `v-bind` shorthand(약어)
  - `:` (colon)

##### Class and Style Bindings

- 클래스/스타일 연결

## Event Handling

### `v-on`

### Modifiers

> Vue 공식문서 체크</br>
> class and style bindings</br>
> event handling</br>
> form input bindings
