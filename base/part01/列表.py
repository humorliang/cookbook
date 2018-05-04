# -*-coding:utf-*-
# 列表格式
wordList = ['i', 'want', 'u', 'have', 12, 'day']  # 列表可以存不同数据类型

# 访问使用索引
print(wordList[2])  # me

# 列表的循环遍历
# 使用for循环
for v in wordList:
    print(v)
print('-------------')

# 使用while循环
i = 0
while i < len(wordList):
    print(wordList[i])
    i += 1

# 列表为可变类型，增删改直接对原列表操作
stu = ['xiaomin', 'xiaoli', 'xiaowu']

# append(obj)添加操作
stu.append('xiaochen')
print(stu)  # ['xiaomin', 'xiaoli', 'xiaowu', 'xiaochen']

# extend(list) 将另一个集合逐一添加到列表中
stu2=['li','zhang']
stu.extend(stu2)
print(stu)  # ['xiaomin', 'xiaoli', 'xiaowu', 'xiaochen', 'li', 'zhang']

# insert(index,obj) 在index位置插入元素obj



