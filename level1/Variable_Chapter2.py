'''
Python VS C++

C++에선 int n = 2;이면 n의 자료형에 맞게 공간을 할당하고 2값에 해당하는 비트를 공간에 넣을 뿐이다.  n <- 2 방향
Python에선 n=2이면 variable_pool에 int(2) 객체가 생기고 여기에 n이란 이름표를 붙인다. n -> 2 방향
즉, 우측 변수항이 주인공이다.


'''


# 기본 선언
n = 700
print(type(n))  # class int

# 동시 선언
x = y = z = 9
print(x, y, z)
print("x is y ??", x is y)
print("y is z ??", y is z)
# 재선언

var = 75
print("var의 처음 id ", id(var))
var = "Changed Value"
# 내용물이 문제가 아니고 자료형 자체가 바뀌었고, 파이썬은 이를 재할당한다.
# 그래서 변수의 주소(pointer)부터 달라졌다.
# C++ 같은 곳에선 아예 삭제를 하지 않으면 불가능하다.

print("var에 string을 넣은 뒤 id ", id(var))
print(var, ' ', type(var))  # class str

# Object Reference: 변수 값이 할당된 상태에서 일어남

# ex1)
print(300)
"""
1. type에 맞는 object 생성      print(int(300)) 300에 맞는 int class의 object 생성
2. 값 생성                      object가 값이 된다.
3. 콘솔 출력
"""
# ex2)
n = 777
print(n, type(n))

'''
1. 777 -> int(777) int class의 object 생성(JAVA의 autoboxing과 유사함)
2. object(value)를 n에 할당한다. (여기 설명방식)
2. n이란 이름표를 object에 붙인다. (열혈파이썬 방식)

여기부터 내 생각임

파이썬에선 변수의 이름보단 값부터 만들어서 이름을 붙이는 방향이다
777이 먼저 처리되어야 n을 고려한다.

auto n = 777; 이런 상황이면 777을 기준으로 auto가 정해진다.
dynamic binding이기 때문에 런타임 중에 자료형이 정해저 컴파일언어가 되기 힘들다.

C++에선 n이란 변수를 먼저 생성한다. 내용물은 없어도 되고 공간 확보만 한다.
그리고 그 공간에 값에 해당하는 비트값을 세겨 놓을 뿐이다. 

int n;
n =777;
이래도 상관없다.

'''


"""
파이썬의 따옴표 주석은 들여쓰기를 따진다. 따라서 어느 block의 주석인지 반드시
구분해야 하기 때문에 쓰고 있는 부분에 맞게 따라서 들여쓰기를 작성해야 한다.

"""

m = n  # m -> 777 <- n      Shallow Copy
print("m is n ?? ", m is n)
m = 400
print("changed m is n ??", m is n, id(m) == id(n))  # False가 뜬다.
print("n value is ", n)
print("m value is ", m)

a = 111  # int(111) object가 생성되고 이를 변수 pool에서 사용해서 메로리를 아낀다.
b = 111  # C++에선 모두 *a *b는 다 다르다.
print(id(a), id(b))
print("a is b?? ", a is b)  # 모두 동일한 instance(class의 object)이다.

# 만약에 C++에서 같은 pointer를 공유하면 한 변수를 변경하면 나머지도 자동으로 변경된다.
# 그러나 여기선 두 변수가 분리될 것이다.

b = 222
print("a is Changed b ?? ", a is b)


# 변수 명명법

"""
camelCase : numberOfCollegeGraduates -> method

PascalCase : NumberOfCollegeGraduates -> class

snake_case : number_of_college_graduates   전부 소문자 -> variable

"""
