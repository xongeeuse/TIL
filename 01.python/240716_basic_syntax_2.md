# 240716

#### 📌 오늘 핵심 주제 
- string

- list(가장 중요)

    - 여러가지 데이터type을 항목(item)으로 가질 수 있다.
    - 중첩 구조를 사용하여 1차원, 2차원, ... n차원 배열 구조를 구현할 수 있다.

            1차원[a, b, c, d]
            2차원[[a,b],[c,d]]
            3차원[[[a,b],[c,d]], [[e,f],[g,h]]]

- range

    - 정해진 범위, 정수 차례로 생성
    - 정해진 횟수만큼 프로그램 반복

- dict

- 논리연산자

- 멤버십 연산자

- 단축평가

#### 어제 복습
- Data types : 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
        
    - int (정수 자료형) *진법 표현 체크*
    - float(실수 자료형) 
        
            *부동 소수점 에러 : decimal 모듈 이용해 해결 가능*
            *지수 표현 방식*

## Sequence Types
### list
> 여러 개의 값을 순서대로 저장하는 *변경 가능*한 시퀀스 자료형

#### list 표현
- 0개 이상의 객체를 포함하며 데이터 목록을 저장
- 대괄호[]로 표기
- 데이터는 어떤 자료형도 저장할 수 있음

### tuple
> 여러 개의 값을 순서대로 저장하는 *변경 불가능*한 시퀀스 자료형
>> 뭐가 불변이라는 것..?
#### tuple 표현
- 0개 이상의 객체를 포함하며 데이터 목록을 저장
- 소괄호()로 표기
- 데이터는 어떤 자료형도 저장할 수 있음
- *요소가 하나인 경우 (1,) 와 같이 표현*

#### 튜플은 어디에 쓰일까?
- 개발자가 직접 사용하기 보다 '파이썬 내부 동작'에서 주로 사용됨
- 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능

### range
> 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

#### range 표현
- range(시작값, 끝값, 증가값)
- range(n) : 0부터 n-1까지의 숫자 시퀀스
- range(n, m) : n부터 m-1까지의 숫자 시퀀스

#### range 특징
- 증가값이 없으면 1씩 증가
- 증가값이 음수면 감소, 증가값이 양수면 증가
- 증가값이 0이면 에러
- 증가값이 음수면 시작값이 끝값보다 커야 함
- 증가값이 양수면 시작값이 끝값보다 작아야 함

- 주로 반복문과 함께 사용 예정!
```python
for i in range(5)
print(i)

# 0
# 1
# 2
# 3
# 4
```

### dict 딕셔너리
> *key-value쌍*으로 이루어진 *순서와 중복이 없는* *변경 가능*한 자료형

#### dict 표현
- key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range ...)
- value는 모든 자료형 사용 가능
- 중괄호{}로 표기
- 순서가 없기 때문에 index 사용도 불가 (key error 뜸)
```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}
print(len(my_dict)) # 2

# 추가
my_dict['banana'] = 50
print(my_dict) # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['banana'] = 1000
print(my_dict) # {'apple': 12, 'list': [1, 2, 3], 'banana': 1000}
```

### set 세트(집합 자료형)
> *순서와 중복이 없는* **변경 가능**한 자료형

#### set 표현
- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호{}로 표기
- 빈 세트는 `my_set_1 = set()`와 같이 표현

#### set 집합 연산
```python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

# 교집합
print(my_set_1 & my_set_2) # {3}
```

### None
> 파이썬에서 '값이 없음'을 표현하는 자료형 (N 대문자로 표기)
```python
variable = None
print(variable) # None
```
### Boolean
#### 불리언 표현 💥
- 비교/논리 연산의 평가 결과로 사용됨
- 주로 조건/반복문과 함께 사용

```python
bool_1 = True

수정 필요!
```

###  Collection
> 여러 개의 항목 또는 요소를 담는 자료 구조 (str, list, tuple, set, dict)

순서가 있으면 시퀀스
순서가 없으면 비시퀀스

## Type Conversion
> 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정 

### 암시적 형변환 Implicit Type conversion
> 파이썬이 자동으로 수행하는 형변환

#### 예시
- 정수와 실수의 연산에서 정수가 실수로 변환됨
- Boolean과 Numeric Type에서만 가능
    ```python
    print(3 + 5.0) # 8.0

    # Boolean에서 True = 1, False = 0

    print(True +3) # 4
    print(True + False) # 1
    ```

### 명시적 형변환 Explicit Type Conversion
> 프로그래머가 아닌 

#### 예시
- str > int : 형식에 맞는 숫자만 가능
    ```python
    print(int('1')) # 1

    # ValueError : invalid literal for int() with base 10: '3.5'
    print(int('3.5))

    print(int(3.5)) # 3 (소수점 자리 버림)
    print(float('3.5')) # 3.5
    ```

- int > str : 모두 가능
    ```python
    print(str(1) + '등') # 1등
    ```

## 연산자
### 산술 연산자
> 사칙 연산 등등

### 복합 연산자
> 연산과 할당이 함께 이뤄짐

### 비교 연산자 
= 은 할당을 의미
== 같음

``` python
# SyntaxWarning: "is" with a literal. Did you mean "=="?
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 때문
# 아래 조건은 항상 False이기 때문에 is 대신 ==를 사용해야 한다는 것을 알림
print(1 is True)  # False
print(2 is 2.0)  # False
print(1 == True)  # True
print(2 == 2.0)  # True
```

### 논리 연산자 👀❓
- and : 논리곱
- or : 논리합
- not : 논리부정

### 평가
#### 단축평가 👀❓👀❓
> 논리 연산에서 두번째 피연산자를 평가하지 않고 결과를 결정하는 동작

### 연산자
#### 멤버십 연산자
> 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인
>> dict의 경우 key 로 접근!

#### 시퀀스형 연산자
> 