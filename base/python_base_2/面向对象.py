# -*-coding:utf-8-*-
# 类和对象

# 类就是创建对象的模板
# 类的构成：
# 类的名称：类名； 类的属性：一组数据  类的方法：允许对对象操作的方法

# 类的定义 大驼峰命名法


class Car:
    def move(self):
        print('车在移动')

    def toot(self):
        print('车在鸣笛')


# 类的实例 也称对象
bmw = Car()
bmw.move()  # 车在移动

# 类的构造函数 __init__()函数


class BigCar:
    # 初始化函数，完成一些默认设定
    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

    def move(self):
        print('车在跑')


bgc = BigCar()
print(bgc.wheelNum)  # 4

# 类的初始化函数接收参数


class NewCar(object):
    def __init__(self, wheelNum, color):
        self.wheelNum = wheelNum
        self.color = color

    def move(self):
        print('车在跑')

    def __str__(self):
        msg = '我是__str__方法'+'车有'+str(self.wheelNum)+'轮子'+'车是'+self.color
        return msg


car = NewCar(4, '红色')

print(car.color)  # 红色


# 魔法方法
# 打印id()
print(NewCar)  # <class '__main__.NewCar'> 类的地址
print(car)  # 我是__str__方法车有4轮子车是红色
print(bgc)  # <__main__.BigCar object at 0x0000026EFF1C4EF0> 打印对象的地址

# 在python中__xxx__()的就是特殊方法，有特殊功能,用print()输出对象时就会调用__str__()方法返回的值

# self 就相当c++中的 this指针 python解释器在运行的时候将对象传递给self


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(self)


person1 = Person('张三', 28)

person1.speak()  # <__main__.Person object at 0x000002C56FD8C208> self的值为当前对象


# 修改属性 隐藏数据
class Person2:
    def __init__(self):
        self.name = '张三'
        self.age = 22

    def setName(self, name):
        self.name = name

person2=Person2()

# 通过对象名直接修改
person2.name='李四'
print(person2.name) # 李四

# 通过方法直接访问
person2.setName('老王')
print(person2.name) # 老王
