
# list
"""
순서O, 중복O, 수정O, 삭제O

"""

a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000.1, 'Ace']
e = [100, 10.3, ['Ace', "Base", 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14]

# indexing

print('>>>> ')
print('d - ', type(d), d)
print('d - ', d[1])
print('e - ', e[-1][1], type(e[-1][1]))


print('e - ', list(e[-1][1]))
# e[-1][1]은 str이기 때문에 iterable object로 list()함수에 넣으면
# 각 index element가 list의 element가 된다.

# list operation

print('>>>> ')
print('c + d', c + d)  # 두 list를 이어 붙인다.
print('c * 3', c*3)  # c의 내부는 유지하되 이어 붙인다.

print("'Test' + str(c[0])", 'Test' + str(c[0]))
# string + int는 TypeError이기 때문에 string + string으로 이어붙인다.

# 값 비교

print(c == c[:3] + c[3:])

# id
temp = c
print("id(temp): ", id(temp))
print("id(c): ", id(c))
# 얕은 복사가 default이다. Object references


# list 수정 삭제

print('>>>>>')
c[0] = 4
print("id(c)=> ", id(c))
c[1:2] = ['a', 'b', 'c']
print("id(c)=> ", id(c))
print('c - ', c)
c[1:2] = [['a', 'b', 'c']]  # 이때 내부 리스트가 들어감
print('c - ', c)
"""
c[0] -> int(70)을 c[0] -> int(4)로 참조하는 객체를 바꾸었다.

c -> [70, 70, 80, 85] == [70] + [70] + [80] + [85] 

c[1:2] == [40]이므로 sublist를 가져온 것이다.

sublist [40] = ['a', 'b', 'c'] 자동 얕은 복사

[어떤 값이든 상관없어] = ['a', 'b', 'c']

c -> [70] + ['a', 'b', 'c'] + [80] + [85]

예시

arr1 = []
arr2 = [1, 2, 3]

arr1 = arr2
print(arr1) ---> [1, 2, 3] 이렇게 나온다.

"""

c[1] = ['a', 'b', 'c']
print('c - ', c)

# 리스트 함수

a = [5, 2, 3, 1, 4]
print('a - ', a)

a.append(10)
a.pop()  # stack처럼

a.reverse()  # 이미 들어있는 요소들을 반대로 배열한다.


print('a - ', a.index(3))  # value의 첫 인덱스를 찾는다. 검색 find 기능

a.insert(2, 7)  # insert(pos, value)

a.remove(3)  # 가장 처음 있는 3을 제거해라

print('a.count() - ', a.count(4))  # 4가 리스트에 몇개 있나?

ex = [8, 9]
a.extend(ex)  # a += ex, a + ex와 같다.
print('a - ', a)
