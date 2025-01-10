// JSX 주의 사항!
// 1. 중괄호 내부에는 자바스크립트 표현식만 넣을 수 있다.
// 2. 숫자, 문자열, 배열 값만 렌더링된다.
    // true, undefined, null 등은 오류를 발생시키진 않지만 화면에 렌더링 X
    // 객체값이 있다면 obj.a 이런 식으로 문자나 숫자값을 렌더링 하도록 접근해야함
// 3. 모든 태그는 닫혀 있어야 한다.


const Main = () => {
    const number = 9;
    const obj = { a: 1 };
    return (
        <main>
            <h1>main</h1>
            <h2>{number % 2 === 0? "짝수" : "홀수"}</h2>
            {10}
            {number}
            {[1, 2, 3]}
            {true}
            {undefined}
            {null}
            {obj.a}
        </main>
    )
}

export default Main;