# -*-coding:utf-8 -*-
# 遍历
# 通过 for...in... 可以遍历 字符串、列表、元组、字典等数据结构

# 字符串遍历
a_str = 'love'
for i in a_str:
    print(i, end=' ')
# l o v e
print('\n')
print('-'*20)

# 列表遍历
a_list = ['2', '3', '4']
for a in a_list:
    print(a, end=' ')
# 2 3 4
print('\n-----------')

# 元组遍历
a_tuple = ('a', 'b', 'c')
for value in a_tuple:
    print(value, end=" ")
# a b c
print('\n---------')

# 字典遍历
info = {'name': 'li', 'age': '23', 'job': 'python'}

# 遍历字典所有的键
for value in info.keys():
    print(value, end=" ")
# age job name
print('\n--------')

# 遍历字典所有的值
for value in info.values():
    print(value, end=' ')
# 23 python li
print('\n--------')

# 遍历字典的所有项,每一项为元组
for item in info.items():
    print(item, end=' ')
# ('age', '23')('job', 'python')('name', 'li')
print('\n--------')

# 遍历字典的key-value（键值对）
for k, v in info.items():
    print('Key:%s,Value:%s' % (k, v), end=' ')
# Key:age,Value:23 Key:name,Value:li Key:job,Value:python
print('\n--------')

# 列表的用法enumerate()
char=['a','b','b']
for i,v in enumerate(char):
    print(i,v)
# 0 a
# 1 b
# 2 b
