# coding:utf-8
# from __future__ import division #导入浮点整除python3之前默认
a=1/2
print(a) # 0.5


# 整除 //
print(1//2) # 0

# 取余 % 
print(10%3) # 1

# 幂运算 **
print(2**2) #4

# 长整型数 3之前 1000000000000000L
print(1000000000000000) # 3之前  出现 interger too large

# 十六进制
print(0xAF) #175

#变量赋值 命名： 字母 数字 下划线  在python中一切皆对象 不能使用关键字
x=2

#语句
sta=2*2

# 本章函数
# abs(number) 返回数字绝对值
print(abs(-10))

# cmath.sqrt(number) 返回平方根 可用于负数
import cmath,math
print(math.sqrt(2))  # 1.4142135623730951 不能用于负数
print(cmath.sqrt(-1)) #1j

# float(object) 提供字符串和数字转换为浮点数
print(float('2.1')) #2.1
print(float(2)) #2.0

# help（） 提供交互式文档
print(help(abs))

# input(proms) 提供用户输入
# inp=input(u'亲输入内容')
# print(inp)

# int(obj) long(obj) 将字符串和数子转换为整型和长整型

# math.ceil(num) 将返回数的上入整数，返回值为浮点数
# math.floor(num) 将返回数的下舍整数，返回值为浮点数

# pow(x,y[,z]) 返回下 x 的 y 次幂 对 z 进行取模
# raw_input(prompt) 获取用户输入返回类型为字符串

# repr(object) 返回字符串的表现形式

# round(number[,ndigits]) 对数字进行四舍五入

# str(obj) 转换为字符串
