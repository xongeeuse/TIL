// math 모듈듈

function add(a, b) {
    return a + b
}

function sub(a, b) {
    return a - b
}

// CommonJS 모듈 시스템 활용용
// module.exports = {
//     add,
//     sub,
// }

// ES 모듈 시스템 활용
export { add, sub }

// 위 방식이 아니라 아래처럼 선언과 동시에 export도 가능
// export function multiply(a, b) {
//     return a * b
// }

// math 모듈의 default 값으로 설정도 가능
export default function multiply(a, b) {
    return a * b
}