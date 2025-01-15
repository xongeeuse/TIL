// 1. lambda
// 람다식은 우리가 마치 value처럼 다룰 수 있는 익명함수
// 정말 익명이라기 보다는 java의 익명함수와 유사

// 1) 메소드의 파라미터로 넘겨줄 수 있다. fun maxBy(a :Int)
// 2) return값으로 사용할 수 있다.

// 람다의 기본 정의
// val lambdaName : Type = {argumentList -> codeBody}

//val square : (Int) -> (Int) = {number -> number*number}
// type 추론할 수 있게 하나는 명시해 줘야 함
val square = {number : Int -> number*number}

val nameAge = {name :String, age :Int ->
    "My name is ${name}, I'm ${age}"
}



fun main() {
    println(square(12))
    println(nameAge("Jiyoung", 32))

    val a = "Jiyoung said, "
    val b = "Joyce said, "
    println(a.pizzaIsGreat())
    println(b.pizzaIsGreat())

    println(extendString("Ariana", 27))
}

// 확장함수
val pizzaIsGreat : String.() -> String = {
    this + "Pizza is the best!"
}

fun extendString(name : String, age : Int) : String {
    val introduceMyself : String.(Int) -> String = { "I am ${this} and ${it} years old."}
        // this가 가리키는 것 => 확장함수 콜하는 오브젝트
        // it => 하나 들어가는 파라미터의 경우, it으로 생략 가능
    return name.introduceMyself(age)
}

// 람다의 Return
// 마지막 한 줄이 반환값 의미

// input param은 여러가지일 수 있으니까 (Int)와 같이 소괄호 묶어주기
// return 값은 type이 하나니까 String 처럼 안써도 돼
val calculateGrade : (Int) -> String = {
    when(it) {
        in 0..40 -> "fail"
        in 41..70 -> "pass"
        in 71..100 -> "perfect!"
        // Int값 인자로 받아 String 반환해야 하는데
        // 위 범위 외의 값 있을 수 있으니까 else 반드시 작성
        else -> "Error"
    }
}

// 람다를 표현하는 여러가지 방법
fun invokeLambda(lambda: (Double) -> Boolean) : Boolean {
    return lambda(5.2343)
}
