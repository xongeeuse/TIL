bㅠ# 241031 Introduction of Vue

## Frontend Development

- 웹사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인하는 것
- HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발

### Client-side frameworks

- 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임워크
- 3대장: `Vue`, `React`, `Angular`

### Single Page Application

- 단일 페이지에서 동작하는 웹 애플리케이션
  > 매 요청마다 백엔드 측에 페이지를 요청하는 것은 아님</br>
  > 프론트엔드 프레임워크의 특징: SPA 기반 개발(페이지가 하나)</br>
  > 첫 요청 때만 페이지 받고 이후에는 데이터만 받음
- (<=> MPA, Multi Page Application)

#### SPA 작동 원리

- 최초 로드 시 필요한 모든 리소스 다운로드
- 이후 페이지 갱신에 *필요한 데이터*만을 _비동기적으로 전달_ 받아 화면에 필요한 부분만 동적으로 갱신
- 페이지 전체를 다시 로드할 필요 X, 필요 데이터만 서버로부터 가져와서 화면에 표시
- JS를 사용해 클라이언트 측에서 동적으로 콘텐츠 생성 및 업데이트
  - `CSR` 방식, Client-side Rendering
    ```
    1. 사용자가 웹사이트에 요청 보냄
    2. 서버는 최소한의 HTML과 JS파일을 클라이언트로 전송
    3. 클라이언트는 HTML과 JS 다운로드
    4. 브라우저가 JS 실행하여 동적으로 페이지 콘텐츠 생성
    5. 필요 데이터는 API 통해 서버로부터 비동기적으로 가져옴
    ```
  - 클라이언트에서 콘텐츠를 렌더링하는 방식
  - (<=> SSR, Server-side Rendering)
