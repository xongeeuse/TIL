fun main() {
    helloWorld()
    println(add(4, 5))

    //3. String Template
    val name = "Jiyoung"
    val lastName = "Song"
    println("My name is $name")
    println("My name is ${name + lastName}")

    // $ 기호로 사용하고 싶을 때는 \$ 와 같이 사용
    println("This is 2\$s")

    /*
    여러줄
    주석은
    이렇게
     */
}

//1. 함수

fun helloWorld() : Unit {       // return 타입 없으면 : Unit 생략 가능
    println("Hello Kotlin World!")
}

fun add(a: Int, b: Int) : Int {
    return a + b
}

//2. val vs var
// val = value 바뀌지 않는 값, 상수
// var = variable 변할 수 있는 값, 변수

fun hi() {
    val a : Int = 10
    var b : Int = 9
    b = 100

    // 자동추론이기 때문에 타입 생략해도 문제 없음
    // but, 할당이 바로 이루어지지 않을 시 타입 명시해야 함

    val c = 50
    var d = 15
    var e : String

    var name : String = "Jiyoung"
    var familyName = "Song"

}