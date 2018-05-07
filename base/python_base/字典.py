# -*-coding:utf-8 -*-
# 字典 是由键：值组成
info = {'name': 'zhang', 'age': 23, 'job': 'python'}

# 键值的访问
print(info['name'])  # zhang
# print(info['na'])  # 键不存在会出现KeyError错误

# 键值访问get的用法
print(info.get('name'))  # zhang
print(info.get('id'))  # None 键不存在时返回None
print(info.get('id', 'Key is Not'))  # 键不存在时返回设置的值'Key is Not'


# 字典的常见操作
# 修改元素
info['name'] = 'li'
print(info.get('name'))  # li

# 添加元素 变量名['键']=数据 键不存在时直接添加，存在就修改
info['id'] = 10
print(info)  # {'age': 23, 'name': 'li', 'id': 10, 'job': 'python'}

# 删除元素  
# del   clear() 删值
del info['name']
print(info)  # {'id': 10, 'job': 'python', 'age': 23}
dic1={'dic':1}
del dic1
# print(dic1) # 字典删除了,报nameError错误
dic2={'dic2':2}
# ######### clear（）清空键值，字典变量名还在
dic2.clear()
print(dic2) # {} 空字典 清空字典内的键值



# 字典的常见操作2

# len()
print(len(info)) # 3

# keys() 所有的键
print(info.keys())  # dict_keys(['id', 'age', 'job'])

# values() 所有的值
print(info.values())  # dict_values(['python', 23, 10])

# has_key 查找键
# print(info.has_key('id')) # AtrributeError Python3没有这个用法python2有
 


