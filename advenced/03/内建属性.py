# coding:utf-8
# 内建属性


class Person(object):
    pass


# 查看内建属性
print(dir(Person))

# 属性说明  触发方式
['__class__',  # 实例所在的类  实例.__class__
 '__delattr__',
 '__dict__',  # 实例自定义属性  vars(实例.__dict__)
 # __del__ 析构   del删除实例
 # __bases__ 类所有父类构成元素 类名.__bases__
 '__dir__',
 '__doc__',  # 类文档子类不继承  help(类或实例)
 '__eq__',
 '__format__',
    '__ge__',
 '__getattribute__',  # 属性访问拦截器  访问属性时
 '__gt__',
 '__hash__',
 '__init__',  # 初始化够着函数   创建实例后赋值使用。在__new__后
 '__le__',
    '__lt__',
    '__module__',
    '__ne__',
 '__new__',  # 生成实例所需属性  创建实例时
 '__reduce__',
 '__reduce_ex__',
 '__repr__',  # 实例字符串表示,准确性  类实例回车或print(repr(类实例))
 '__setattr__',
 '__sizeof__',
 '__str__',  # 实例字符串表示,可读性  print(实例)没实现使用repr
 '__subclasshook__',
 '__weakref__']
