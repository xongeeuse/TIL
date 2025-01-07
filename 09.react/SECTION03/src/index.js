// console.log("안녕, Node.js")


// const moduleData = require("./math")

// console.log(moduleData.add(1, 2))
// console.log(moduleData.sub(1, 2))


// 구조분해할당 활용
// const { add, sub } = require("./math")

// commonJS > ES로 변경하면서 require 아니라 export-import 사용
import mul from "./math.js"         // default 함수 이렇게 import 가능
import { add, sub } from "./math.js"

// import문 하나로 합쳐서도 가능
// import mul, { add, sub } from "./math.js"
console.log(add(1, 2))
console.log(sub(1, 2))
console.log(mul(2, 3))

import randomColor from "randomcolor"

const color = randomColor()
console.log(color)