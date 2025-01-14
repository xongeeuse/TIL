open class Human constructor(val name : String = "Anonymous") {
    // constructor 생략 가능
    // java와 비교해 굉장히 간결한 부분^ 클래스 선언과 변수 동시에 일어나니까

    //부 생성자
    // 주 생성자가 있기 때문에 this로 위임 받는 과정 필요
    constructor(name : String, age: Int) : this(name){
        // this 통해서 위임받아오고
        println("My name is ${name}, ${age}years old.")
    }

    // 생성과 동시에 코드블럭 실행
    // 주 생성자의 일부로 가장 먼저 실행
    init {
        println("New human has been born!")
    }

//    val name = "Jiyoung"

    // 객체 생성할 때 이름을 생성하고 싶다면?
    // ^ 클래스 선언 시 constructor 넣어주거나
    // 그 과정에서 바로 val 할당도 가능
    // default 값 지정도 가능
//    val name : String = name

    fun eatingCake() {
        println("This is so YUMMYYYYYY.")
    }

    open fun singASong() {
        println("lalala~")
    }
}

// 동일 파일 내에 있어도 open 해줘야 클래스 받아올 수 있음
// 부모 클래스를 자식에게 오버라이딩?
// 상속받은 메서드를 이 클래스에서 특수하게 사용하고 싶을때 오버라이드
// 상속은 클래스 하나만 가능
class Korean : Human() {

    override fun singASong() {
        super.singASong()
        println("라라라~")
        println("My name is ${name}.")
    }

}

// kotlin java 차이점
// 파일 이름과 클래스 이름 일치하지 않아도 되고
// 여러 클래스도 한 파일 안에 작성 가능


fun main() {
//    val human = Human("Minsu")
//    val stranger = Human()
//    human.eatingCake()

    val mom = Human("Kyuri", 52)

//    println("This human's name is ${human.name}.")
//    println("This human's name is ${stranger.name}.")

    val korean = Korean()
    korean.singASong()
}

