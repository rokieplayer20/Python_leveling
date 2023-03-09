
# def function_name(parameters):
#   code


def first_function(w):
    print("Hello", w)


word = "Good boy"

first_function(w=word)
print("type of function is ", type(first_function))


# class "function"

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


x, y, z = func_mul(11)
print(x, y, z)


def func_nest(x, y):

    return x(y)


print(func_nest(func_mul, 22))
"""

python에선 함수, 객체 무엇이든 입력으로 넣고 
반환할 수 있다.

함수 내부에서 class도 선언할 수 있고
새로이 함수도 선언하고 반환할 수 있다.


"""

# packing/unpacking: *args, **kwargs

# 함수 선언 할 때 입력 순서: 일반변수, *args, **kwards


def args_func(*args):  # 매개변수 이름은 아무거나 상관없다.
    print('type of *args is', type(args))
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------------')


args_func('Lee')
# 만앨 args이면 Lee를 문자열로 보고 글자 하나하나 다룬다.
# 그러나 *args를 사용하면 tuple로 보고 'Lee'를 0번 index로 본다.

args_func('Lee', 'park')

"""
여러 인지를 넣으면 tuple로 묶어서 입력했다고 보고
함수 내부에서 tuple로 사용할 수 있다.

"""


def kwargs_func(**kwargs):
    print("type of **kwargs is", type(kwargs))

    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('=============')


kwargs_func(name1="lll", name2="pppp", use=False)

# 이렇게 짝지어서 입력하면 dick 형태로 받아들이다.


def all_func(arg_1, arg_2, arg_3="arg3", *args, **kwargs):
    print(arg_1, arg_2, arg_3, args, kwargs)


all_func(1, 2, "this is 3", '4', '5', True, age1=20, age2=30)

# 함수 선언 할 때 입력 순서: 일반변수, *args, **kwards

# default 값을 정해도 일반 인자에서 다 안 입력했을 때밖에 쓸모 없더라
# 맨뒤로 빼도 사용할 수 없고, arg_3 = "this"이렇게 지정해도 앞에
# 뒤에 비슷한 문법이 있어서 위치상 쓸 수 없다고 나온다.


# nested function

def nested_func(num):
    # 여기서 선언한 함수는 지역변수다. object
    def func_in_func(num):
        print(num)
    print("In func")

    func_in_func(num + 100)

    # 그러나 return 해서 값을 복사한다.
    return func_in_func


any_func = nested_func(100)

any_func("this is any func!")


a = 3
b = [4, 5, 6]


def edition(inner_variable, inner_list):

    inner_variable += 9
    inner_list.append(9)


print("Before a and b are ", a, b)  # 3, [4, 5, 6]

edition(a, b)

print("After a and b are ", a, b)  # 3, [4, 5, 6, 9]

"""
a의 값이 변경되지 않는다.

shallow_capy.png 그림을 보면 같은 int(3)을 가리켜도 다른 이름표(변수)이다.

namespace가 다르기 때문에 서로 다른 지역변수다.


"""

# lambda expression

# 일반 함수: 객체 생성 -> 리소스(메모리) 할당

# 람다: 즉시 실행함수(Heap 초기화) -> 메모리 초기화

# 남발하면 가독성이 오히려 감소한다.


def Annie(x, y): return x+y

# Annie = lambda x,y: x+y 자꾸 변형되어서 따로 주석함


print("type of Annie is ", type(Annie))  # class "function"


"""

이름(선택사항) = lambda 매개변수들 : code

"""


def func_final(x, y, func=1):
    print(">>>", x*y*func)


func_final(2, 3, (lambda x, y: x+y)(1, 1))

func_final(y=12, x=1)
"""
순서대로 입력하지 않을 거라면 무슨 매개변수에 무엇을 넣었는지 하나하나 명시할 수 있다.

2, y=2 처럼 넣을 수 있다. 모두 명시할 것이 아니라면 명시하는 것은 반드시 뒤에 있어야 한다.

앞의 나머지 매개변수는 순서를 지킨다.


"""


# Hint: foctor type, return type을 지정해 놓을 수 있다.


def tot_length1(word: str, num: int) -> int:
    return len(word) * num


def tot_length2(word: str, num: int) -> None:
    print('hint exam2: ', len(word) * num)


tot_length2("123", 2)

print("type of None is ", type(None))  # NoneType


# input

# name = input("Enter Your Name")
# year = int(input("when? ")) input의 기본 타입은 문자열이다.

print(
    "FirstName - {0}, LastName - {1}".format(input("FirstName: "), input("LastName: ")))
