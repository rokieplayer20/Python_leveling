'''
int: 정수
float: 실수
complex: 복소수
bool: 불리언
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 딕셔너리

'''
from glob import escape
import math
import sys


list_1 = [1, 2, 3]
tuple_1 = (1, 2, 3)  # tuple = 2, 3, 5처럼 괄호 없어도 튜플로 본다.
set_1 = {3, 4, 56}
dict_1 = {"2": 1, "3": 33}


# number: int, float32, float64
"""
알아둬야 할 연산자

abs(x) 절댓값

pow(x, y) == x**y

"""


# Python에서 overflow를 방지하고 더 큰 공간을 할당한다.
# C에선 메모리 크기가 정해진 fixed-precision을 사용한다.
# Python은 arbitrary-precision을 사용해서 필요하면 메모리를 더 끌어와 사용할 수 있다.

# 주의, 판다스나 넘파이 같은 곳에선 C 스타일이기 때문에 overflow를 고려해야 한다.
i = 1
i2 = 999999999999999999999999999999999999
print("i size is ", sys.getsizeof(i))
print("i2 size is ", sys.getsizeof(i2))
print(i, type(i))
print(i2, type(i2))

# type transformation 형변환

ex = i + 1.1
print(ex, type(ex))
# 자동 형변환이 더 큰 쪽으로 일어난다. 실수가 double(64bits)가 기본으로 본다.

a = 3.
b = 6
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))  # 실수 -> 정수 : 버림이 기본이다.
print(int(d))
print(int(True))
print(float(False))
# 문자열도 수로 바꿔준다. 다만, 문자열을 쓰면 두번째 허수부를 입력할 수 없다.
print(complex(3, 1), complex('3'))
# C에서 0: false, 0 외 다른 수:true로 본다.
# false: 0000....000, true: 00000.....00001 이렇기 때문이다.


print(abs(-5))
x, y = divmod(100, 8)
print(x, y)  # x 몫, y 나머지

# 외부 모듈

print(math.ceil(5.1))  # 5.1보다 큰 정수 중에서 가장 작은 정수 -> 소숫점 올림
print(math.pi)


# 문자열

str1 = "I am Python"
str2 = 'Python'
# 따옴표 3개 있어도 주석 외에도 안에 있는 문자열을 선언할 수 있다.
# len(str4) == 10 따옴표는 세지 않고 1개짜리 따옴표와 동일한 기능을 제공함
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))  # 전부 class 'str'

# 빈 문자열
str_t1 = ''  # 또는 ""
str_t2 = str()

# escape charactor 이스케이프 문자
print("I'm Boy", 'I\'m Boy')  # \ 역슬레쉬

escape_str1 = "Do you have a \"retro games\""
print(escape_str1)

# Raw String : r'' 안의 모든 확장이 없이 있는 그대로 표시할 수 있다.

raw_s1 = r'D:\python\test'
print(raw_s1)

# Multi-line input: 여러줄에 걸쳐서 한 번에 입력하는 것이다.

# \를 줄을 중간에 끊고 사용하면 다음 line에서 변수를 마저 이어준다.
multi_str1 = \
    """this is
 Python
  multi-line test.
  """
multi_str2 = \
    '1 line ' \
    '2 line'

print(multi_str1)
print(multi_str2)


# 문자열 연산 + * []

str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul INC Busan"
print(str_o1 * 3)  # *
print(str_o1 + str_o2)  # +
print('y' in str_o1)  # 시퀀스 자료형은 in을 사용할 수 있다.
print('n' not in str_o2)
print(str_o1[1:])  # []


# 문자열 형 변환
print(str(66))
print(str(True), type(str(True)))  # boolean을 넣어도 'True' 문자열이 된다.

# 문자열 함수

print("capitalize: ", str_o1.capitalize())  # 첫 글자를 대문자로
print("endswith: ", str_o2.endswith('e'))  # 마지막 문자가 내가 원하는 것이 맞는지 True False

print("replace ", str_o1.replace("thon", "good"))  # 특정 부분을 찾아서 치환한다.
print("sorted ", sorted(str_o1))  # 정렬 후 list로 반환한다.
# str object는 sort함수 없다.


print("split: ", str_o4.split(' '))  # 어떤 기준으로 쪼개서 리스트로 반환한다.


# 반복(시퀀스)

im_str = "Good boy!"

# print(dir(im_str))
# dir()로 method를 찾아보면 __iter__가 있다면 iterable object로써 반복문에 쓸 수 있다.
# 시퀀스 형은 슬라이스 연산이 가능하다.
for i in im_str:
    print(i)


# slicing

str_s1 = "Nice Python"

print(str_s1[::-1])
# 인덱스 0부터 마지막까지를 거꾸로 1씩 추린 substring이 나옴
print(str_s1[1:9:2])
print(str_s1[-5:])  # ython

# ASCII code

a = 'z'
print(ord(a))  # 'z'의 아스키 코드는 122다.
print(chr(122))  # 아스키코드를 넣으면 문자로 만들어준다.



