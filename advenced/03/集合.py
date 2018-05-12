# coding:utf-8
# 集合与之前列表、元组类似，可以存储多个数据，但是这些数据是不重复的

# 集合对象还支持union(联合),
# intersection(交),
# difference(差)
# sysmmetric_difference(对称差集)等数学运算.
# set(iterable)
x = set([1, 2, 3])
y = set([2, 4, 3])
print(x)  # {1, 2, 3}
print(type(x))  # <class 'set'>

# 交集
print(x & y)  # {2, 3}

# 并集
print(x | y)  # {1, 2, 3, 4}

# 差集 在x中不在y中的
print(x-y)  # {1}

# 对称差集  在x或y中 不是两者共有的元素
print(x ^ y)  # {1, 4}
