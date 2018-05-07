# -*-coding:utf-8-*-
# 公共方法
# 运算符
# 运算符       描述     支持的数据类型
#   +         合并      字符串，列表，元组
#   *         赋值      字符串，列表，元组
#  in         判断      字符串，列表，元组，字典
# not in      判断      字符串，列表，元组，字典

a = 'I'
b = 'love'
print(a+b)  # Ilove

print(b*2)  # lovelove

if 'o' in b:
    print('o在b内')  # o在b内

# python内置方法

# cmp(item1,item2) 比较两个值
# print(cmp('hello','love')) # python3 没有该函数

# len(item) 计算容器的长度
print(len(b))  # 4

# max(item) 计算容器的最大值
# min(item) 计算容器的最小值
aList = [12, 3, 4, 43, 48]
print(max(aList))  # 49
print(min(aList))  # 3


# 多维列表或者元组的访问
aLi = [['a', 'b'], ['c', 'd']]
print(aLi[0][0])  # a
