# coding:utf-8
# 内建函数

# 常用内建函数
# range() python2中是一个列表  pytho3中是一个迭代值

# range(start,stop[,step]) 开始 结束 步长 默认步长为1
print(range(5))  # range(0, 5)
for i in range(0, -5, -1):  # 可以为负值
    print(i, end=' ')  # 0 -1 -2 -3 -4

print('\n-------------')
# map() 根据提供的函数对指定序列做映射
# map(fun,sequence[,squence,...]) ->list
# function: 是一个函数
# sequence: 是一个或多个序列, 取决于function需要几个参数
# 返回值是一个list
list1 = map(lambda x: 2*x, [1, 2, 3])
print(list1)
list2 = map(lambda x, y: x+y, [1, 2, 3], [2, 3, 4])
print(list2)

# filter() 会对指定序列执行过滤操作
# filter(function or None, sequence) -> list, tuple, or string
# function:接受一个参数，返回布尔值True或False
# sequence: 序列可以是str，tuple，list
print(filter(lambda x: x % 2, [1, 2, 3, 4, 5]))

# reduce() 函数会对参数序列中元素进行累积
# reduce(function, sequence[, initial]) -> value
# function: 该函数有两个参数
# sequence: 序列可以是str，tuple，list
# initial: 固定初始值
# python3里该函数被放在 from functools import reduce
from functools import reduce
print(reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd'))  # ddaabbcc

# sorted() 排序默认
# sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
# key 按什么规则排序  reverse反转 默认从小到大
print(sorted([2, 5, 3, 1, 4, ]))  # [1, 2, 3, 4, 5]


