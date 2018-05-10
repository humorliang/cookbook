# coding:utf-8
# 装饰器
# 在不影响函数功能扩展的情况下对功能进行扩展

# 装饰器也是一个函数,相当于高阶函数 ,函数也可以当成变量引用


def w1(fun):
    def inner():
        print('---w1功能--')
        fun()
    return inner


# @w1
def fun1():
    print('fun1')

# 装饰器的本质
# fun1=w1(fun1) <=等同于=> @w1


# 验证w1
fun1()
# ---w1功能--
# fun1

# 装饰器的应用场景
# 引入日志
# 函数执行时间统计
# 执行函数前预备处理
# 执行函数后清理功能
# 权限校验等场景
# 缓存

# 装饰带参数的函数和返回值的装饰器
# 通用函数


def w2(fun):
    def inner(*args, **kwargs):
        print('---装饰函数带参数的装饰器---')
        return fun(*args, **kwargs)
    return inner
# 函数带参数的装饰


@w2
def fun2(a, b):
    print('fun2')
    print(a+b)
    return a+b


# w2装饰器验证
print(fun2(2, 3))

print('--------')
# 装饰器带有参数


def w3(a='aa'):
    def wrap(fun):
        print('装饰器传来的参数', a)

        def inner(*args, **kwargs):
            print('w3装饰器')
            return fun(*args, **kwargs)
        return inner
    return wrap


@w3(a='hello')
def fun3(a, b):
    print('fun3')
    return a+b


print(fun3(2, 3))
# 装饰器传来的参数 hello
# w3装饰器
# fun3
# 5
print('---------')
# 多个装饰器装饰函数


def a(fun):
    def inner(*args, **kwargs):
        print('----a装饰器----')
        return '<a>'+str(fun(*args, **kwargs))+'</a>'
    return inner


def b(fun):
    def inner(*args, **kwargs):
        print('----b装饰器----')
        return '<b>'+str(fun(*args, **kwargs))+'</b>'
    return inner


@a
@b
def fun4(a, b):
    print('fun4')
    return a+b


print(fun4(2, 3))
# 在执行到a装饰的时候，把下面的看成一个整体，然后b装饰好以后返回给a再装饰
# ----a装饰器----
# ----b装饰器----
# fun4
# <a > <b > 5 < /b > </a >


# 类装饰器
# 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
# 在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，那么这个对象就是callable的。

class W(object):
    def __init__(self, fun):
        print('init')
        print('func name is %s' % fun.__name__)
        self.__fun = fun

    def __call__(self,a):
        print('---装饰器的功能----')
        # 相当于函数装饰器中执行一边函数 fun
        self.__fun(a)
#说明：
#1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
#    并且会把test这个函数名当做参数传递到__init__方法中
#    即在__init__方法中的func变量指向了test函数体
#
#2. test函数相当于指向了用Test创建出来的实例对象
#
#3. 当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法
#
#4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
#    所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体

@W
def test(a):
    print(a)
    print('test')


test(1)
# init
# func name is test
# ---装饰器的功能----
# 1
# test
