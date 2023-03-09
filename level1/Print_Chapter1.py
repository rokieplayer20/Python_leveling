# 따옴표 3개로도 나온다 잘 안 쓴다.
import sys
print('''Python''')
print("""Python""")

# separator option
print('P', 'Y', 'T', 'H', 'O', 'N')  # sep=' '가 default이다.
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')  # 각각 ,로 분리하지만 끝은 적용되지 않음
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')

# end option
print('Welcome', 'to', end=' ')
print("city")  # end의 default는 end='\n'이지만 끝부분 처리 문자를 지정할 수 있다.


# file option 나중에 더 다룬다.
print('Learn Python', file=sys.stdout)  # stdout으로 출력해라 이게 default다

# format 사용 (d: int, s: string, f: float)
#
print("%s %s" % ('one', 'two'))
print("{} {} {}".format("one", 'two', 3.14))  # 자료형이 자동으로 맞춰진다
print('{1} {0}'.format(3, 5))  # {}는 index 0부터 맞춰지나 내가 조절할 수 있다.

# %s 사용법
print('%10s' % ('nice'))  # 10자리수 문자열 오른쪽 정렬이 디폴트다.
print('{:>10}'.format("nice2"))  # 위의 것과 동일

print('%-10s' % ('nice'))  # 10자리수 문자열 좌측정렬
print('{:10}'.format("nice2"))  # 위의 것과 동일

print("{:_>10}".format("nice"))  # 10자리 우측정렬이며 빈곳은 _(원하는 문자)로 채워
print('{:^10}'.format("nice2"))  # 중앙정렬

print("%5s" % ("very nice"))
print("%.5s" % ("very nice"))  # 5자리를 만들어도 .을 붙여야 절삭해서 출력한다.

print('{:10.5}'.format('pythonStudy'))  # 좌측정렬 10자리를 출력하되 5글자로 절삭


# %d
print("%d %d" % (1, 2))
print("%4d" % (2345))
print("{:4d}".format(12))  # 문자열일 경우 d s f 같은 거 안 썼다. s가 디폴트라서

# %f
print("%.8f" % (1234.123456789))  # 소수부 8자리
print('{:f}'.format(3.143525452))  # 디폴트 자리수가 있어서 잘린다.

# 주의 총 6자리 중 소수부 2자리 빈곳 0
print('%06.2f' % (2.7142342345))
print('{:06.2f}'.format(2.7142342345))
