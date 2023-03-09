import sys
import inspect
# from ..sub2 import module2

# module2.py


def mod1_test1():
    print("Module1 -> Test1")
    print("Path : ", inspect.getfile(inspect.currentframe()))
    # 현재 실행 프래임의 파일 위치를 나타냄


def mod1_test2():
    print("Module1 -> Test2")
    print("Path : ", inspect.getfile(inspect.currentframe()))
