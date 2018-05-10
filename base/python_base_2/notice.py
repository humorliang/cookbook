# coding:utf-8
# 给程序传参
import sys
print(sys.argv)


# 列表推导式
# 轻量级循环创建列表
# 1.基本方式
a = [x for x in range(4)]
print(a)  # [0, 1, 2, 3]
a = [x for x in range(3, 10)]
print(a)  # [3, 4, 5, 6, 7, 8, 9]


# 在推导式中使用if
a = [x for x in range(2, 15) if x % 2 == 0]
print(a)  # [2, 4, 6, 8, 10, 12, 14]

# 在推导式中使用两层for循环
a = [(x, y) for x in range(3) for y in range(2)]
print(a)
#[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


# python3 的range(start,stop,speed) 为一个可迭代对象
# python2 的range(start,stop,speed) 为一个列表

# 将[1,2,3,...,100]变成[[1,2,3],[4,5,6],...]
a = [x for x in range(100)]  # 生成[1,2..,100]
print([x for x in range(0, 100, 3)])  # [0, 3,.,99]
b = [a[x:x+3] for x in range(0, 100, 3)]  # 使用切片公具进行a列表的切片生成子列表
print(b)

print('---------')
# 集合类型
# 集合内的元素不能够重复]
# set 可以帮助list快速去重
a = set([1, 2, 3])
print(type(a))  # <class 'set'>


# set list tuple之间相互转换
c = [1, 2, 3]
print(type(c))  # list
print(list(c))

print(type(set(list(c))))  # set
