# coding:utf-8
# 你可以将它赋值给一个变量
# 你可以拷贝它
# 你可以为它增加属性
# 你可以将它作为函数参数进行传递

# 类也是对象也可以动态的创建它


def choose_class(name):
    if name == 'foo':
        class Foo():
            pass
        return Foo
    else:
        class Bar():
            pass
        return Bar


# type()函数创建类
# type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）
Test = type('Test', (), {})
print(Test)  # <class '__main__.Test'>
help(Test)

# 元类
# 元类就是用来创建类的“东西”。元类就是类的类
# Python中所有的东西，注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类
# type就是创建类对象的类。你可以通过检查__class__属性来看到这一点。
age = 34
print(age.__class__)  # <class 'int'>
# type就是Python的内建元类,可自己创建元类
print(age.__class__.__class__)  # <class 'type'>


# __metaclass__属性 自定义元类时使用没有就使用内建type创建类
# class Foo(object):
#     __metaclass__ = something
# 1.Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
# 2.如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
# 3.如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
# 4.如果还是找不到__metaclass__, Python就会用内置的type来创建这个类对象

# 自定义元类
# 元类的主要目的就是为了当创建类时能够自动地改变类

def upper_attr(future_class_name, future_class_parents, future_class_attr):

    # 遍历属性字典，把不是__开头的属性名字变更为大写
    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith('__'):
            newAttr[name.upper()] = value

    # 调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'

# 元类的本质就是：
# 1.拦截类的创建
# 2.修改类
# 3.返回修改之后的类

print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True

f = Foo()
# print(f.BAR)  # bip

# 动态语言：可以在运行的过程中，修改代码

# 静态语言：编译时已经确定好代码，运行过程中不能修改
# __slots__ 变量限制实例添加属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Person(object):
    __slots__=('name','age')

p=Person()
p.name='老王'
# p.score=60 #AttributeError: 'Person' object has no attribute 'score'
print(p.name)


