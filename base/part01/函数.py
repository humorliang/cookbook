# -*- coding:utf-8 -*-
# 函数
# 定义函数


def demo():
    print('定义了一个函数')


# 函数调用
demo()

# 函数文档说明


def doc():
    """
    这是函数文档说明
    """
    print('函数文档的定义')


# 函数声明的查看help函数
print(help(doc))

# 函数的参数
# 定义有参函数


def fun(a, b):
    """
    两数相加
    Arguments:
        a {int} -- [description]
        b {int} -- [description]
    """
    sum_ = 0
    sum_ = a+b
    return sum_


# 带有参数的调用
value1 = fun(1, 2)
print(value1)  # 3
# 指定传参调用
value2 = fun(b=1, a=3)
print(value2)  # 4

# 小案例，三个数的平均值


def avgNum(a, b, c):
    avg = (a+b+c)/3
    return avg


# 三个数的平均值
print(avgNum(1, 3, 5))  # 3.0

# 局部变量

# 全局变量
gl = 10


def varFun():
    # 局部变量
    a = 10

    # 全局变量修改
    global gl  # 不可变类型修改全局时
    gl = 100
    print('我是局部变量a=%d' % a)
    print('我是局部变量gl=%d' % gl)


# 我是局部变量a=10
# 我是局部变量gl=100
varFun()

# 函数进行多值返回


def rMore():
    a = 0
    b = 1
    return a, b


print(rMore())  # (0, 1)

# 缺省参数：调用时没有传参，则使用默认
# 带有默认参数一定要位于参数列表的最后面


def missArgu(a, b=10):
    sum_ = a+b
    return sum_


print(missArgu(2))  # 12

# 不定长参数 *args ,**kwargs


def arKw(a, b, c=3, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
    print('kwargs:')
    for k, v in kwargs.items():
        print('key:', k, end=',')
        print('value:', v, end=';')


arKw(1, 2, 34, 4, m='a', n='b')
# a: 1
# b: 2
# c: 34
# args: (4,)
# kwargs:
# key: n, value: b
# key: m, value: a

print('\n')
# 引用传参 ：引用是地址的引用
# 不可变类型引用，可变类型引用
# 不可变类型：str,tuple,num
# 可变类型：list,dict,set
a_str = 'a'
b_list = []


def quoteFun(a, b_lsit):
    b_list.append(a)
    a = 'aa'


quoteFun(a_str, b_list)
print(a_str)  # a 不变
print(b_list)  # ['a'] 改变


# 递归函数
# 在自己内部调用自己的函数

# 递归函数应用
# 求 N 的阶乘
def recursion(num):
    if num > 1:
        return num*recursion(num-1)
    else:
        return 1


print(recursion(3))  # 6
# 汉诺塔游戏


def hannoi(num, a, b, c):
    """汉诺塔函数

    Arguments:
        num {盘子数量} -- 序号从上到下依次递增
        函数的三个参数对应三个坑，分别表示开始，辅助,目标，递归调用时要考虑哪个柱子
        要起到什么作用，然后放入对应的坑。
        a {开始的位置，a柱子} -- 开始的位置
        b {辅助的位置，b柱子} -- 辅助的位置
        c {目标的位置，c柱子} -- 目标的位置
    """
    if num == 1:
        print('第'+str(num)+'个'+a+"->"+c)
    else:
        # 递归调用的时候要注意哪个是开始的柱子，辅助的柱子，目标柱子
        hannoi(num-1, a, c, b)  # 找辅助盘 想把num-1从 a->b要借助 c做辅助盘
        print('第'+str(num)+'个'+a+"->"+c)
        hannoi(num-1, b, a, c)  # 找辅助盘 想把num-1从 b->c要借助 a做辅助盘


hannoi(2, 'a', 'b', 'c')


# 匿名函数 返回表达式的值
# 语法：lambda [arg1[,args2...argsN]] :expression

def sumAll(a, b): return a+b


print(sumAll(1, 3))  # 4

# 应用场景
stuList = [
    {'name': 'zhang', 'age': 23},
    {'name': 'wu', 'age': 19},
    {'name': 'li', 'age': 27}
]
stuList.sort(key=lambda x: x['name'])  # 按名字排序
# [{'name': 'li', 'age': 27}, {'name': 'wu', 'age': 19}, {'name': 'zhang', 'age': 23}]
print(stuList)
stuList.sort(key=lambda x: x['age'])  # 按年龄排序
# [{'name': 'wu', 'age': 19}, {'name': 'zhang', 'age': 23}, {'name': 'li', 'age': 27}]
print(stuList)
