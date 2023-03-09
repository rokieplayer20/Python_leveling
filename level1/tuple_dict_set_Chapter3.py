
# tuple: immutable

# 순서O, 중복O, 수정X, 중복X

import copy
a = ()
b = tuple()

# 주의! 원소가 1개일 때는 tuple이 아닌 다른 자료형으로 본다.
#  그래서 ,가 필요하다.
aa = (1)
bb = (1,)
print("type(aa) is ", type(aa))
print("type(bb) is ", type(bb))

c = (11, 12, 13, 14)
d = (100, 1000., 'Ace', 'Base', 'Captine')
e = (100, 1000., ('Ace', 'Base', 'Captine'))

print('>>>>>>>>')
print('d - ', d[1])

print('list(e[-1]): ', list(e[-1]))  # tuple is iterable.

# d[0] = 1111 tuple은 재할당을 지원하지 않아 TypeError가 뜬다.

print('d[0:2] : ', d[0:3])  # tuple slicing은 subtuple을 내놓음

# tuple 연산, 리스트와 똑같다.

print('>>>>>>>>>')
print('c + d : ', c + d)
print('c*3 : ', c*3)

# tuple 함수

a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a.index(3) - ', a.index(3))
print('a.count(2) - ', a.count(2))

# packing and unpacking

# packing: 묶었기 때문에 index로 접근할 수 있다.

t = ('foo', 'bar', 'baz', 'qux')

# unpacking: 묶여 있던 것을 풀어서 순서에 맞게 변수를 대입한다.

(x1, x2, x3, x4) = t  # 괄호가 없어도 되지만 관례상 쓴다. C++의 tie()를 의식해보자.

print(f'x1, x2, x3, x4 == {x1}, {x2}, {x3}, {x4}')
print(
    f'type(x1), type(x2), type(x3), type(x4) == {type(x1)}, {type(x2)}, {type(x3)}, {type(x4)}')


# 괄호를 안 써도 튜플로 인식

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 내부에 원소로 리스트 같은 게 있을 때를 위해서 깊은 복사를 똑같이 지원한다.
# 단, copy, deepcopy 모두 튜플 안에 가변 변수가 있어야 한다.
# 안 그러면 그냥 깊은 복사가 적용되지 않는다.
g1 = (1, 3, [2, 3, 45])
g2 = copy.deepcopy(g1)
print('g1 is g2 ??', g1 is g2)


# Dictionary: json 형태, hash 적용된 자료형

# 순서x, key 중복 x, 수정o, 삭제 o

p1 = {'name': 'Kim', 'phone': '010', 'birth': '87412'}
p2 = dict({1: 'Lee'})
# key: 숫자, 문자열
# value: 다 됨
print('p2 - ', p2)

# 공식문서 선언방식이지만 불편하다.

# 2차원으로 리스트[[key:value], []], 튜플(()), 혼합 [(), ()], ([], [])을
# dict constructor에 넣으면 된다.

p3 = dict([['alice', 2], ['bob', 34]])  # 이것이 본구조에 가깝다.

# unpacking에서 ** 두 번 풀어주는 이유

p4 = dict(
    carey=3,
    dovey=5,
    estella=7
)  # class constructor 방식
p4['foxy'] = 9

print('p3 - ', p3)
print('p4 - ', p4)  # key를 자동으로 key로 본다.


# 출력

print('p1.get("name1") - ', p1.get('name1', 'no_name'))

# get()은 해당 값이 없으면 None을 반환하거나 디폴트 값을 내가 지정해서
# 코드의 예외를 방지할 수 있다.


p1['address'] = 'gugugu'  # 추가
p1['address'] = 'korea'  # 수정

# traverse: keys(), values(), items()

print('p1.values() - ', p1.values())
print('p1.keys() - ', p1.keys())
print('p1.items() - ', p1.items())  # [(), (), ()] 형태

for k, v in p1.items():  # [(), (), ()] 리스트에서 튜플을 꺼내서 자동 언패킹이 된다.
    # x1, x2, x3 = t2 자동 언패킹
    print('k, v - ', k, v)


print('p1.pop("adderess") - ', p1.pop('address'))  # list 때와 같다

print("p1.popitem() - ", p1.popitem())  # 임의의 item을 pop한다.


print('"birth" in p1 - ', "birth" in p1)


# method로 수정하는 방법

p1.update(name='kane')  # key는 immutable 객체이기 때문에 굳이 ''를 안 써도 된다. 그러나 비추천한다.
print('p1 - ', p1)

temp = {"name": "gane"}
p1.update(temp)         # update는 이 방식을 추천한다.
print('p1 - ', p1)


# set
# 순서x, 중복x, 수정o, 삭제o

s1 = set()

s2 = set([1, 2, 3, 4])
s3 = set([1, 4, 5, 6])
s4 = set([1, 2, 'Pen', 'Cap', (1, 2, 3)])
s5 = {'foo', 'bar', 2, 2.3}  # key:value 형식이 아니면 집합이다.

print('s4 - ', type(s4), s4)

print('s5 - ', type(s5), s5)

print('foo in s5 ??', 'foo' in s5)

ts = tuple(s4)  # list(s4) iterable object는 하나씩 분리해서 담김
print(ts)

print('len(s4) == ', len(s4))

# 집합 연산 다 된다.

# 이미 연산자 오버라이드되어 있고 자바처럼 객체 매소드가 있다.
print('s3 & s2 == ', s3 & s2, s3.intersection(s2))

print('s3 | s2 == ', s3 | s2, s3.union(s2))

print('s3 - s2 == ', s3 - s2, s3.difference(s2))

print('s3 ^ s2 == ', s3 ^ s2, s3.symmetric_difference(s2))  # XOR

# 같은  원소가 있는지 확인 TF

print('s2 & s3 ==  vacant ?', s2.isdisjoint(s3))

# 부분집합인지 TF

print('s2 --> s3 ??', s2.issubset(s3))

print('s2 <--- s3 ??', s2.issuperset(s3))


# 추가 제거

s1.add('7')
s1.add('ppap')
print('s1 == ', s1)
s1.remove('ppap')
print('s1 == ', s1)

s1.discard('7')
# remove와 다르게 없는 원소릴 지우려 해도 KeyException을 발생시키지 않음

s2.clear()  # 전부 지워
