"""
__dict__ : class의 attribute 딕셔너리

dir(class 이름) : named_method 및 사용자의 함수 list

method call -> class_name.method(intance, parameters) -> instance.method(parameters)
"""

# 모든 class는 object class를 상속한다.
# 'class Dog:' 이라고 생략해도 된다.

# namespace: 객체를 인스턴스화 할 때, 저장되는 공간


class Dog(object):

    # class 변수 (C++: static public variable)
    species = "firstdog"

    # 초기화/인스턴스 속성
    # constructor 역할을 수행하는 named method이다.
    def __init__(self, name, age):

        self.name = name
        self.age = age


print(Dog, '//', type(Dog))  # '__main__.Dog' // class 'type'

# C++의 main 함수 역할을 하는 py파일이면 __name__ == '__main__'이 된다.

a = Dog("chichi", 2)
b = Dog("Dabit", 3)
c = Dog("chichi", 2)

# 비교

print("a==b, a is b : ", a == b, a is b)
print("a == c, a is c : ", a == c, a is c)

# 복합자료형이 가변 변수를 가지고 있을 때
# 이를 서로에게 복사하면 얕은 복사가 나타난다.
# bb = aa = [1, 2, [2]]

# 그러나 초기화를 따로따로 하면 다 깊은 복사가 된다.
aa = [1, 2, [2]]
bb = [1, 2, [2]]
print(f"id(aa) == {id(aa)}, id(bb) =={id(bb)}")
print(f"id(aa[2]) == {id(aa[2])}, id(bb[2]) =={id(bb[2])}")

print(aa is bb)

# namespace

print("dog1", a.__dict__)  # class의 attribute를 dictionary로 나타낸다.
print("dog2", b.__dict__)
# Class 변수인 species는 안 나온다. 개별 인스턴스의 네임스페이스에 있는 것이 아니기 때문이다.
# a, b의 명칭공간을 내놓으라


print(Dog.species)  # JAVA의 static public 변수
print(Dog.__dict__)
# 'species: 'firstdog'으로 Dog class의 명칭공간에 들어가 있다.


# self: instance 자신에 대한 포인터 객체, C++과 JAVA의 this 역할

class SelfTest:

    # class method: C++과 JAVA의 static public method로 봐라
    def func1():
        print('Func1 call')

    def func2(self):
        print('Func2 call')


f = SelfTest()
"""

SelfTest f = new SelfTest();였던 것이 축약되었다.
동적할당 constructor

SelfTest f(); 정적할당 constructor

print(dir(f)) 
내부에 이미 있는 함수와 내가 선언한 함수들을 한 번에 볼 수 있다.



"""


"""

f.func1()
이렇게 실행하면 인수가 없어야 하는데 1개가 있다고 오류가 나온다.
자동으로 f.func1(self) 이렇게 실행된 것이다.

여기서 self는 f(instance)를 요구한다.

class.func1(f) 이런 식으로 호출되어 문제가 된 것이다.
SelfTest.func1(f)

차이가 있다면 C++, JAVA에선 instance의 유무에 무관하게
class.method() 혹은 instance.method() 무엇이든 호출이 가능하다. 
"""

# method call의 방식이다.
# class_name.method(intance, parameters)
SelfTest.func1()

SelfTest.func2(f)  # SelfTest.func2()로 호출하면 인수가 1개 없다고 예외다.


# 클래스 변수, 인스턴스 변수

class Warehouse:
    # class_variable
    stock_num = 0

    def __init__(self, name):  # constructor
        # instance_variable
        self.name = name
        # "stock_num += 1"로 쓰면 UnboundLocalError: local variable 'stock_num' referenced before assignment
        Warehouse.stock_num += 1

    def __del__(self):  # destructor소멸자 객체가 소멸할 때 호출되는 네임드 메소드: del instance
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Joe')

print(f"Warehouse.stock_num == {Warehouse.stock_num}")
print(f'user1.stock_num == {user1.stock_num}')
del user2

print(Warehouse.stock_num)

""""
여기에서 알 수 있는 것

class 변수는 class이름 혹은 intance이름으로 꺼낼 수 있지만

class method는 오직 class이름으로만 호출할 수 있다. 왜냐하면 형태가 자동으로 바뀌어 self 인자의 유무 때문이다.
JAVA에선 상관없었다.



"""
print("__dict__ 차이점: instance.__dict__ VS class_name.__dict__")
print(user1.__dict__)
print(Warehouse.__dict__)

print("---- dir() 차이점:  set(dir(instance)) - set(dir(class_name)) ------")
print(set(dir(user1)) - set(dir(Warehouse)))
"""

dir(Warehouse)보다 dir(user1)이 이전 내용을 포함하여 더 큰 list를 갖고 있다.

반면에 user1.__dict__는 Warehouse.__dict__와 공통으로 갖지 않는 자신만의 고유한 차이점만 갖는다.
모든 method나 클래스변수는 공통사항이기 때문에 class_name.__dict__에 들어간다.


"""


class Dog2:
    species = "secondDog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old.'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


C = Dog2('july', 4)

print(C.info())
print(C.speak("WOW"))
