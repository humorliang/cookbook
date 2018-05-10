# coding:utf-8
# == 、is
# is 是比较两个引用是否指向了同一个对象（引用比较）。id值是否相同
# == 是比较两个对象是否相等。

# 浅拷贝、深拷贝

# 浅拷贝：
# 是拷贝对象的引用,没有拷贝值
a = [1, 2, 3]
b = a  # 浅拷贝
print(id(b))  # 3128600082504
print(id(a))  # 3128600082504

# 深拷贝
# 对一个对象所有层次的拷贝
import copy
m = [1, 2, 3]
n = copy.deepcopy(m)
print(id(m))  # 1386553148296
print(id(n))  # 1386553113544

# 进制

# 进制之间的转换
# 十进制转二进制
print(bin(10))  # 0b1010

# 二转十
print(int('1010', 2))

# 十转八
print(oct(9))  # 0o11
# 八转十
print(int('022', 8))  # 18
# 十六转十
print(int('0x12', 16))  # 18
# 十转十六
print(hex(18))  # 0x12

# 位运算
# & 按位与
# | 按位或
# ^ 按位异或
# ~ 按位取反
# << 按位左移
# >> 按位右移


# 私有化
# xx: 公有变量
# _x: 单前置下划线, 私有化属性或方法，from somemodule import *禁止导入, 类对象和子类可以访问
# __xx：双前置下划线, 避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
# __xx__: 双前后下划线, 用户名字空间的魔法对象或属性。例如: __init__, __ 不要自己发明这样的名字
# xx_: 单后置下划线, 用于避免与Python关键词的冲突

# 属性property 取代getter和setter方法

# @property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，主要有2个作用
# 将方法转换为只读
# 重新实现一个属性的设置和读取方法, 可做边界判定
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Money(object):
    def __init__(self):
        self.__money = 0

    # 方法只读
    @property
    def money(self):
        return self.__money

    # 设置
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('error:不是整形数字')


mon = Money()
print(mon.money)  # 0
mon.money = 80
print(mon.money)  # 80
