# 240717

## 📌 오늘 핵심 주제
- 변수명과 객체
- copy, deepcopy
    ```python
    # Python Tutor 이용해서 제대로 이해하기

    a = 3
    b = a

    import copy

    c = copy.deepcopy(a)

    d = [1, 2, 3]
    e = d

    g = copy.deepcopy(d)

    t1 = [[1, 2, 3], ['a', 'b', 'c']]
    t2 = t1
    t3 = t1[:]
    t4 = copy.deepcopy(t1)
    ```

- 함수 정의와 호출
> 함수는 코드 재사용을 위해 만듦, class는 코드 + 변수 재사용하기 위해서 만듦

    - 매개변수와 인자
    - 가변 인자를 쓰는 이유(고객정보)

   ```python
   #다시 확인해주..

   def save_new_customer(id, pw, *args):
        print(f'{id}=')
        print(f'{pw}=')
        print(args)
        
    save_new_customer('sky', '1234') # tel, age
    save_new_customer('', '1234')
   ```

- 함수와 스코프
- 글로벌 LEGB Rule
- map(), zip()
    ```python
    # map(함수의 이름, 복수의 데이터)
    def print_num(a):
        print(a)

        map(print_num, [1, 2, 3])   # 1 2 3
        map(float, [1, 2, 3])   # 1.0 2.0 3.0

    ```

    ```python
    zip(A, B)

    zip A = [a, b, c, d]
    zip B = [1, 2, 3]
    ```


- lambda
    ```python
    def make_sum(a, b):
        return a + b

        x = lambda a, b : a + b
        print(x(3, 5))  # 8

        # lambda, map 함께 쓰는 법도 이해하기
        # map(lambda a : print(a), [1, 2, 3])
    ```

### 함수 Functions
> 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

#### 함수를 사용하는 이유
- 코드의 중복을 방지
- **재사용성**이 높아지고, 코드의 **가독성**과 **유지보수성** 향상

#### 함수 구조

> parameter input (x) > output f(x) : 반환값 return value

docstring = document string
함수에 대한 설명서, 사용법

함수 정의(정의)
```python
def greet(name) :
    """입력된 이름 값에 인사를 하는 메세지를 만드는 함수"""

    message = 'Hello, ' + name
    return message

result = greet('Alice')
print(result)
```

    `def`로 함수 정의 시작
    : 다음에 들여쓰기되는 블록에 작성
    함수가 종료되는 시점 `return`
    함수의 이름과 소괄호를 활용해 호출(call) - function_name(arguments)

```python
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2


result = make_sum(100, 30)
return_value = print(result)
print(return_value)     # None

# # `print`함수는 return값이 없다. None이 출력됨..
# # 그냥 출력이 될 뿐.


def my_func():
    print('hello, world')

result = my_func()  #hello, world
print(result)   #None


```

#### 매개변수와 인자
1. 매개변수 parameter
- 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

2. 인자 argument
- 함수를 호출할 때, 실제로 전달되는 값

```python

# 예시 가져오기

```

- Positional Arguments (위치 인자)
    
    - 함수 호출 시 인자의 위치에 따라 전달되는 인자
    - 위치인자는 함수 호출 시 반드시 값을 전달해야 함

    ```python
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')

    greet('Harry', 20)
    greet(20, 'Harry')
    ```
- Default Argument Values
    - 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

    ```python
    def greet(name, age=20):
        print(f'안녕하세요, {name}님! {age}살이시군요.')

    greet('Bob')    # 안녕하세요, Bob님! 20살이시군요.
    greet('Charlie, 40')    # 안녕하세요, Charlie님! 40살이시군요.
    ```

- Keyword Arguments
    - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
    - 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
    - 단, 호출 시 *키워드 인자는 위치 인자 뒤에 위치해야 함*

    ```python
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')

    greet(name='Dave', age=35)
    greet(age=35, name='Dave')
    # greet(age=35, 'Dave')   # SyntaxError: positional argument follows keyword argument
    ``` 

- Arbitrary Argument Lists
    - 정해지지 않은 개수의 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 '*'를 불여 사용하며, 여러 개의 인자를 tuple로 처리
    ```python
    def calculate_sum(*args):
        print(args)
        print(type(args))

    calculate_sum(1, 100, 5000, 30)
    ```
    


- Arbitrary Keyword Argument Lists
    - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리
    - kwargs = keyword arguments    

    ```python
    def print_info(**kwargs) :
        print(kwargs)

    print_info(name='Eve', age=30)
    ```

#### 인자의 모든 종류를 적용한 예시
    - 위치 > 기본 > 가변 > 가변키워드
    - 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
    - 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

# pos1: 1
# pos2: 2
# default_arg: 3
# args: (4, 5, 6)
# kwargs: {'key1': 'value1', 'key2': 'value2'}
```

### 재귀 함수
> 함수 내부에서 자기 자신을 호출하는 함수
factorial

#### 재귀 함수 예시 (팩토리얼)
```python
𝑛!
𝑛 ∗ (𝑛−1)!
𝑛 ∗ (𝑛−1) ∗ (𝑛−2)!
…
```
- factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출
```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)
# 팩토리얼 계산 예시
print(factorial(5))  # 120
```

----

#### 재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

#### 재귀 함수를 사용하는 이유
- 문제의 자연스러운 표현
  - 복잡한 문제를 간결하고 직관적으로 표현 가능

- 코드 간결성
  - 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음

- 수학적 문제 해결
  - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

#### 재귀 함수 활용 시 기억해야 할 것
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록


### 내장 함수 (Built-in function)
> 파이썬이 기본적으로 제공하는 함수 (별도의 import 없이 바로 사용 가능 ex. `print`, `len')

[내장함수 참고](https://docs.python.org/ko/3.9/library/functions.html?highlight=%EB%82%B4%EC%9E%A5%20%ED%95%A8%EC%88%98#built-in-functions)

```python
numbers = [1, 2, 3, 4, 5]

print(len(numbers)) 
print(max(numbers))
print(min)


