# 📌241029 Asynchronous JavaScript

## 동기/비동기

### Synchronous, 동기

- 프로그램의 실행 흐름이 순차적으로 진행
- 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식

### Asynchronous, 비동기

- 특정 작업의 실행이 완료될 때까지 기다리지 않고 다음 작업을 즉시 실행하는 방식
- 작업의 완료 여부를 신경 쓰지 않고 _동시에 다른 작업들을 수행할 수 있음_

> JavaScript는 병렬적으로 처리하는 비동기식 프로그래밍을 진행할 수 있다!

- 병렬적 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 백그라운드에서 실행되며 빨리 완료되는 작업부터 처리
- 그래서 콜백함수들이 병렬적으로 처리됨!

### Single Thread 언어, JavaScript

- 작업을 처리할 때 실제로 작업을 수행하는 주체
- multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
- JavaScript가 동작할 수 있는 환경 - `브라우저` 또는 `Node.js`
- JavaScript는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경 필요

> 런타임의 시각적 표현 (p.23- 38 참고)

### 브라우저 환경에서의 JavaScript 비동기 처리 동작 방식

1. 모든 작업은 Call Stack(후입선출)으로 들어간 후 처리
2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도 처리
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(선입선출)에 순서대로 들어감
4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 먼저 처리되어 들어온) 작업을 Call Stack으로 보낸다!

### 비동기 처리 동작 요소

- Call Stack
  - 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
  - 기본적인 JavaScript의 Singlt Thread 작업 처리
- Web API
  - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경
  - 시간이 소요되는 작업을 처리(setTimeout, DOM Event, 비동기 요청 등)
- Task Queue(Callback Queue)
  - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
- Event Loop
  - 태스크(작업)가 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고,
  - 처리할 태스크가 없는 경우엔 잠드는, 끊임없이 돌아가는 자바스크립트 내 루프
  - Call Stack과 Task Queue를 지속적으로 모니터링
  - Call Stack이 비어있는지 확인 후, 비어있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

#### 정리

- JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 진행
- 하지만 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨!
- 결국 환경의 도움이 필요하다! 브라우저나 Node.js 같은!
- 동작 원리에 초점을 맞추셔라! 직접 구현하는 거 아님!

## Ajax

- 비동기적인 웹 애플리케이션 개발을 위한 기술
- XMLHttpRequest 기술을 사용해 복잡하고 동적인 웹 페이지를 구성하는 프로그래밍 방식
- 브라우저와 서버 간의 데이터를 비동기적으로 교환하는 기술
- Ajax를 사용하면 페이지 전체를 새로고침 하지 않고도 동적으로 데이터를 불러와 화면을 갱신할 수 있음
- Ajax의 'x'는 XML이라는 데이터 타입을 의미하긴 하지만, 요즘은 더 가벼운 용량과 JavaScript의 일부라는 장점 때문에 JSON을 많이 사용

### Ajax 목적

- 비동기 통신
  - 웹 페이지 전체를 새로고침하지 않고 서버와 데이터를 주고 받을 수 있음
- 부분 업데이트
  - 전체 페이지가 다시 로드되지 않고 HTML 페이지 일부 DOM만 업데이트
  - 페이지의 일부분만 동적으로 갱신할 수 있어 사용자 경험이 향상
- 서버 부하 감소
  - 필요한 데이터만 요청하므로 서버의 부하를 줄일 수 있음

### XMLHttpRequest 객체(XHR)

- 웹 브라우저와 서버 간의 비동기 통신을 가능하게 하는 JavaScript 객체
- JavaScript를 사용해 서버에 HTTP 요청을 할 수 있는 객체
- 웹 페이지 전체 새로고침 없이도 서버로부터 데이터를 가져오거나 보낼 수 있음
- 이름에 XML이라는 데이터 타입이 들어가긴 하지만 XML 뿐만 아니라 모든 종류의 데이터를 가져올 수 있음 > 요즘은 대부분 JSON

## Axios, 엑시오스

> 프론트엔드 프레임워크 Vue에서 장고 혹은 백엔드 서버로 요청을 보낼 때 axios 사용
> 이후 자바스크립트로 비동기적 요청을 서버로 보낼 때 활용하게 될 것

- 브라우저와 Node.js에서 사용할 수 있는 promise 기반의 HTTP 클라이언트 라이브러리
- XHR 객체 생성하고 요청하고 응답까지!

#### then / catch

```JavaScript
      const promiseObj = axios({
        method: "get",
        url: "https://api.thecatapi.com/v1/images/search",
      })
        .then((response) => {
          console.log(response);
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
```

- `then(callback)`
  - 요청한 작업이 성공하면 callback 실행
  - callback은 이전 작업의 성공 결과를 인자로 전달 받음
- `catch(callback)`
  - then()이 하나라도 실패하면 callback 실행(남은 then은 중단)
  - callback은 이전 작업의 실패 객체를 인자로 전달 받음

## Callback과 Promise

### then 메서드 chaining의 장점

- 가독성
- 에러 처리
- 유연성
- 코드 관리

### Promise가 제공하는 이점

1. 실행 순서의 보장
   - 콜백 함수: JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 전에는 호출되지 않음
   - Promise: then/catch 메서드의 콜백 함수는 Event Queue에 배치되는 순서대로 엄격하게 호출됨
   - 이는 비동기 작업의 실행 순서를 더 예측 가능하게 만듦
2. 유연한 비동기 처리
3. 체이닝을 통한 연속적인 비동기 처리
4. 에러 처리의 일원화

### `Promise`

- 비동기 프로그래밍의 복잡성을 줄이고, 코드의 가독성과 유지보수성을 높이는 강력한 도구
- 실행 순서 보장, 체이닝, 에러 처리 등의 특징을 통해 콜백 지옥을 피하고 더 체계적인 비동기 코드 작성을 가능하게 함
