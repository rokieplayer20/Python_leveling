"""
Module: 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
"""


def add(x, y):
    return x+y


def substact(x, y):
    return x - y


def mutiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def power(x, y):
    return x**y


print('__name__을 사용하지 않고 import 하면 아래의 code들이 자동으로 실행된다.')
print('-' * 15)
print("called inner!")
print(add(5, 5))
print(f'__name__ == {__name__}')

print('-'*15)

if __name__ == '__main__':
    print('이 파일을 직접 실행할 경우에만 아래의 코드들이 실행되어야 한다.')
    print('C++의 main함수 역할을 하는 py file이라면 __name__은 __main__이다. \
        아니라면 그냥 파일이 이름이다. \
    ')
