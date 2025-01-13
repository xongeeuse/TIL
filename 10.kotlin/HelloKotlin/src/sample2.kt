fun main() {
//    checkNum(1)
//    checkNum(3)
//    checkNum(9)
//    forAndWhile()
    nullcheck()
}

//4. 조건식

fun maxBy(a: Int, b: Int) : Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}

// 삼항연산자 대신 아래와 같이 표현 가능
fun maxBy2(a: Int, b: Int) = if (a>b) a else b

fun checkNum (score : Int) {
    when(score) {
        0 -> println("This is 0.")
        1 -> println("This is 1.")
        2, 3 -> println("This is 2 or 3.")
        else -> println("I don't know.")
    }

    var b = when(score) {
        1 -> 1
        2 -> 2
        else -> 3
        // else 써줘야 when을 expression으로 사용 가능
    }

    println("b : ${b}")
    when (score) {
        in 90..100 -> println("You're genius.")
        in 10..80 -> println("Not bad.")
        else -> println("Okay.")

    }
}

// Expression vs Statement
// Expression? 뽀짝뽀짝해서 값을 만들면 표현식
// Statement? 값을 만들지 않고 실행하면? 문장
// 코틀린의 모든 함수는 Expression => 아무것도 리턴하지 않는 것 같아도 Unit 반환
// 자바에서는 Void 라는 리턴 값 없는 함수 형태가 존재 => Statement


// 5. Array와 List
// Array ? 메모리가 할당되어 나옴. 정해진 사이즈 있음
// List ?
    // (Immutable) List 수정 불가, 읽기전용
    // MutableList 수정 가능

fun array() {
    val array :Array<Int> = arrayOf(1, 2, 3)
    val list :List<Int> = listOf(1, 2, 3)

    val array2 : Array<Any> = arrayOf(1, "d", 3, 4f)
    val list2 : List<Any> = listOf(1, "d", 11L)

    array[0] = 3
//    list[0] = 2 는 불가능, 읽기전용, 아래와 같이 가져오기는 가능하지만 변경은 불가
    // list는 interface임
    val result = list.get(0)

    val arrayList = arrayListOf<Int>()
    arrayList.add(10)
    arrayList.add(20)

//    arrayList = arrayListOf()
}

// 6. For / While

fun forAndWhile() {
    val students = arrayListOf("Joyce", "James", "Jennie", "Jiyoung")
//    for (name in students) {
//        println("$name")
//    }
    for ((index, name) in students.withIndex()) {
        println("${index + 1}번째 학생 : ${name}")
    }

    var sum: Int = 0
    for (i in 1..10) {
        sum += i
    }
    println(sum)

    var index = 0
    while(index < 10) {
        println("current index : ${index}")
        index++
    }
}

// 7. Nullable / NonNull

fun nullcheck() {
    //NPE : Null pointer Exception
    var name : String = "jiyoung"
    var nullName : String? = null
    // ? 붙여주면 nullable type이 됨 => type 생략하면 안되겠죠?

    var nameInUpperCase = name.toUpperCase()

    var nullNameInUpperCase = nullName?.toUpperCase()

    // ?: 엘비스 연산자
    // 디폴트 값을 주고 싶다면 사용
    val lastName : String? = null
    val fullName = name + " " + (lastName?: "No lastName")
    println(fullName)
}

    // !!
    // nullable이긴 한데 이거 null아니야! 라고 보장
    // 확실하게 null이 아니지 않은 이상 사용 지양하는게 좋음 but, 넘 편해서 자주 씀!

fun ignoreNulls(str : String?) {
    val mNotNull : String = str!!
    val upper = mNotNull.toUpperCase()
}