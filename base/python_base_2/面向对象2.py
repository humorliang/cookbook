# -*-coding:utf-8 -*-

# 保护对象属性
# 1.对象名.属性名=数据  --> 直接修改
# 2.对象名.方法名  --> 间接修改

# 保护属性： 设置私有属性 添加一个外部访问的方法


class People(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


# 创建对象
people = People('隔壁老王')
# print(people.__name)  # AttributeError 私有属性外部无法访问
print(people.getName())  # 隔壁老王
people.setName('隔壁小李')
print(people.getName())  # 隔壁小李


# 特殊方法 __del__
class Animal(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('%s动物对象被删除了' % self.name)


dog = Animal('狗')
# 删除狗对象
# 控制台打印__del__()函数内容 # 狗动物对象被删除了
del dog


# 继承
# 私有的属性，不能通过对象直接访问，但是可以通过方法访问
# 私有的方法，不能通过对象直接访问
# 私有的属性、方法，不会被子类继承，也不能被访问
# 一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用

# 单继承
print('--------------')


class Father:
    def money(self):
        print('老王父亲的100块钱')

    def car(self):
        print('老王父亲的车')


class FatherB:
    def moneyB(self):
        print('老李父亲的100块钱')

    def car(self):
        print('老李父亲的车')


class Son(Father):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('说话')


son = Son('小王')

son.money()  # 老王父亲的100块钱

print('-----多继承-----')


class SonB(Father, FatherB):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eat')


sonB = SonB('小张')

sonB.money()
sonB.moneyB()

# 若两个类的方法名相同时：根据类对象的索引顺序进行先后调用
# (<class '__main__.SonB'>, <class '__main__.Father'>, <class '__main__.FatherB'>, <class 'object'>)
print(SonB.__mro__)

# 类名相同时优先使用靠前的类方法，自身有不用父类
sonB.car()  # 老王父亲的车

# 方法的重写
# 子类的方法跟父类的方法名相同时，会优先调用子类的方法

# 重写父类方法，调用父类方法


class Fa(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('-----Fa------')


class So(Fa):
    def __init__(self, name):
        # 调用父类的__init__方法1：
        # Fa.__init__(self,name)
        # 调用父类的__init__方法2：
        # super(So,self).__init__(name)
        # 调用父类的__init__方法3：
        super().__init__(name)

    def getName(self):
        return self.name


son = So('刘德华')

print(son.name)  # 刘德华
print(son.getName())  # 刘德华


# 多态：定义时的类型跟运行的时候不一样
# python '鸭子类型'

class F1(object):
    def show(self):
        print('---F1----')


class S1(F1):
    def show(self):
        print('----s1---')


class S2(F1):
    def show(self):
        print('-----s2----')

# 多态函数 因为python的函数参数不需要指定类型


def Func(obj):
    print(obj.show())


s1 = S1()
Func(s1)  # ----s1----

s2 = S2()
Func(s2)  # -----s2----


# 类属性、实例属性
# 类对象所拥有的属性叫类属性。实例属性拥有的属性叫做实例属性

class Peo(object):
    name = 'make'  # 公有的类属性
    __age = 23  # 私有的类属性
    moneny = 100


p = Peo()

p.moneny = 200  # 实例属性 与类同名时会覆盖类属性
print(p.moneny)  # 200
print(p.name)  # make
# print(p.__age) # 私有类属性实例外界无法访问
print(Peo.name)  # make
# print(Peo.__age)  # 私有类属性类对象也外界无法访问


# 类方法和静态方法
# 类方法用装饰器@classmethod来装饰标识其为类方法
class Peo2(object):
    country = 'china'

    # 类方法用classmethod来进行装饰
    # 对于类方法第一个参数为类对象，一般用cls作为参数
    @classmethod
    def getCountry(cls):
        return cls.country


p2 = Peo2()
print(p2.getCountry())  # china 实例调用类方法
print(Peo2.getCountry())  # china 类对象调用类方法

print('--------------')
# 静态方法
# 通过@staticmethod来进行修饰，不需要多定义参数


class Peo3(object):
    country = 'china'

    @staticmethod  # 静态方法
    def getCountry():
        return Peo3.country  # 引用类属性时必须通过类对象引用


peo3 = Peo3()
print(peo3.getCountry())  # 实例对象调用
print(Peo3.getCountry())  # 类对象调用
