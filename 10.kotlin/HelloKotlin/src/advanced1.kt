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
    return name.introduceMyself(age)
}
