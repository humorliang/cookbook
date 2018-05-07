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
