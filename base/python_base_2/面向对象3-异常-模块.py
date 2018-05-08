# -*-coding:utf-8 -*-
# 工厂模式
# 1.简单工厂模式
# 1.1 通过函数实现

# 定义辉腾车


class HuitengCar(object):
    def move(self):
        print('车在动')

    def stop(self):
        print('停车')

# 定义途观车


class TugunaCar(object):
    def move(self):
        print('车在动')

    def stop(self):
        print('停车')

# 定义生成具体的对象


def creatCar(typeName):
    if typeName == '辉腾':
        car = HuitengCar()
    elif typeName == '途观':
        car = TugunaCar()
    return car


# 定义一个销售大众的店
class CarStore(object):
    def order(self, name):
        # 生产车
        car = creatCar(name)
        return car

# 1.2 使用类实现
# 定义一个生产汽车的类，汽车生产工厂


class CrearFactory(object):
    def creatCar(self, typeName):
        if typeName == '辉腾':
            car = HuitengCar()
        elif typeName == '途观':
            car = TugunaCar()
        return car


class CarStore2(object):
    def __init__(self):
        # 设置4s店的指定生产汽车的工厂
        self.carFactor = CrearFactory()

    def order(self, typeName):
        # 让工厂根据类型生产车
        car = self.carFactor.creatCar(typeName)
        print('car', car)
        return car

# 工厂方法模式

# 定义一个基础的4s店类


class CarStoreB(object):

    # 定义一了这个方法，并没有实现它，具体在子类中进行实现
    def creatCar(self, typeName):
        pass

    def order(self, typeName):
        # 让工厂根据类型生产
        self.car = self.creatCar(typeName)
        # 根据客户订单的车让它跑起来

    def move(self):
        self.car.move()

# 定一个奥迪4s店


class AodiCarStore(CarStoreB):
    def creatCar(self, typeName):
        self.carFactory = CarFactory2()  # 制定汽车厂
        return self.carFactory.creatCar(typeName)  # 返回车

# 奥迪Q5汽车类


class AodiQ5Car(object):
    def move(self):
        print('-----Q5的move---')

# 奥迪A3汽车类


class AodiA3Car(object):
    def move(self):
        print('----A3的move---')


# 定义一个汽车工厂类,根据订单进行生产


class CarFactory2(object):
    def creatCar(self, typeName):
        self.typeName = typeName
        if self.typeName == '奥迪A3':
            self.car = AodiA3Car()
        elif self.typeName == '奥迪Q5':
            self.car = AodiQ5Car()
        return self.car


# 找一个
aodiA3 = AodiCarStore()
aodiA3.order('奥迪A3')
aodiA3.move()  # 让订单车辆跑起来

# __new__方法和__init__方法
# __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
# __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# 我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节

# 我相当于制造商

# python3中不写object对象默认也会继承object对象


class A(object):
    # 我相当于原料加工环节
    def __init__(self):
        print('这是init函数')

    # 我相当于原料采购环节
    def __new__(cls):
        # 我至少要有一个cls参数，代表要实例化的类
        # 此参数由解释器自动提供
        # 重写__new__方法的时候要点用父类的__new__方法否则无法
        # 创建实例对象
        print('我是new方法')
        return object.__new__(cls)  # 父类返回创建的实例的引用


A()  # 我是new方法 这是init函数

# 单例模式
# 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，
# 这个类称为单例类，单例模式是一种对象创建型模式。


class Singleton(object):
    __instance = None

    def __new__(cls, name):
        # 对这个实例引用进行判断__intsance
        # 没有实例过就创建，否则就直接返回创建过的实例
        # cls当前类对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


name1 = Singleton('张三')
name2 = Singleton('李四')
# 两个实例指向相同
print(id(name1))  # 2292394358600
print(id(name2))  # 2292394358600

name1.age = 12  # name1实例添加一个属性
print(name2.age)  # 12 name2实例同时也获得一个age属性

# 创建单例时只执行一次__init__方法


class Singleton2(object):
    __instance = None
    __init__first = False

    def __init__(self, name):
        if not self.__init__first:
            self.name = name
            self.__init__first = True

    # 这里接受实例化的参数,会传递到__init__()
    # 参数相当于原料:买哪些原料   根据原料进行加工
    def __new__(cls, name):
        # 对这个实例引用进行判断__intsance
        # 没有实例过就创建，否则就直接返回创建过的实例
        # cls当前类对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


na1 = Singleton2('张三')
na2 = Singleton2('李四')
print(na1.name)  # 张三
print(na2.name)  # 张三

na1.age = 18
na2.age = 19
print(na1.age)  # 19
print(na2.age)  # 19
