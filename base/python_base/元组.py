# -*- coding:utf-8-*-
# 元组与列表类似，但是元组元素不能修改，tuple()
aTuple = ('a', 1, 2, 3)

# 访问元素
print(aTuple[1])  # 1

# 不能修改元组，包括删除

# 内置函数 count(),index()

print(aTuple.index('a', 0, 3))  # 0
print(aTuple.count(1))  # 1
