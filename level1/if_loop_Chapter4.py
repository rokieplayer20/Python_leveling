
# if

"""
True : 0이 아닌 수, 비어 있지 않은 str, list, tuple

False: 0, "", [], () ....


"""

from collections import deque
if 'any string':
    print("'any string' is True")


# 산술, 관계, 논리 연산자들 우선순위

# 산술 > 관계 > 논리

print('e1 :', 3+12 > 7 + 3)

print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10)

# indent: 4번 space == \t tab 1개


e = {"name": "Lee", "city": "ICN"}

if "name" in e:
    print("dictionary의 in은  key가 기준이다.")

if "ICN" in e.values():
    print("values() method는 sequence 객체를 반환한다.")


# for

# for in <colloction>:
#   <loop body>

for v1 in range(1, 10, 2):  # 0 <= v1 < 10 범위에서 2개씩
    print("v1 : ", v1)

# range: class 'range' is iterable.

print('1-1000 sum : ', sum(range(4, 1001, 4)))
# sum, min, max


# iterable type: str, list, tuple, set, dict

# iterable return function:
# range, reversed, enumerate, filter, map, zip, sorted

names = ['kim', 'park']

for name in names:
    print('You are ', name)

lotto_numbers = [11, 19, 21, 28, 36, 37]

word = "Noot"

for w in word:
    print("w is ", w)

for n in word:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

    if not n.isalpha():
        break

# continue

lt = ['1', 2, 5, True, complex(1, 23)]

for n in lt:
    if type(n) is bool:
        # type을 비교할 때 type(n) == "bool"도 좋지만
        # type(n) is bool로 해도 된다.
        continue
    elif type(n) is not int:
        continue
    print(n)


# for-else 구문

numbers = [1, 4, 67, 8, 3, 12, 34]

for num in numbers:
    if num == 12:
        print("Found : ", num)
        break
    # else가 if와 같은 들여쓰기가 아니기 때문에 if 다음으로 실행되지 않음
else:
    print('Not Found: ', num)
# list의 모든 원소를 반복한 뒤에 마지막으로 1번 실행된다.
# 만일 for문 속의 break나 return에 걸리면 실행되지 않음

# 변환 예제2

name2 = 'Aceman'
print('Reversed ', reversed(name2))
print('List, ', list(reversed(name2)))

# while <expr>:
#   <statement(s)>

a = ['ff', '23der', 'baz']

while a:
    # a.length() > 0과 같다.

    print(a.pop(0))
    # list.pop()은 index를 명시적으로 입력해 사용할 수 있다.
    # 단지 default가 -1이었을 뿐이다.


aa = deque([1, 2, 4])
print(aa[1])  # append, appendleft, pop, popleft, [index] 다 된다.


# while-else

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print("else out.")

# for-else와 똑같다.
