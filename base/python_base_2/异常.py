# -*-coding:utf-8 -*-
# 异常
# 异常的捕获
# Exception是所有异常的基类
try:
    a = 2/0
    print(a)
except Exception as e:
    print(e)  # division by zero

try:
    print(2/0)
except Exception as e:
    print(e)
finally:
    print('我都会执行')

# 自定义异常并抛出


class StrLenException(Exception):
    '''自定义的异常类'''

    def __init__(self, length, atleast):
        super().__init__()
        self.length = length
        self.atleast = atleast


def main():
    try:
        strN = 'qwer'
        if len(strN) > 3:
            raise StrLenException(len(strN), 3)
    except StrLenException as e:
        print('字符长度为%d,最小长度%d' % (e.length, e.atleast))
    else:
        print('没有异常发生')


main()  # 字符长度为4,最小长度3
