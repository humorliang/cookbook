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
stu2 = ['li', 'zhang']
stu.extend(stu2)
print(stu)  # ['xiaomin', 'xiaoli', 'xiaowu', 'xiaochen', 'li', 'zhang']

# insert(index,obj) 在index位置插入元素obj
a = [1, 2, 3, 4]
a.insert(1, '1')
print(a)  # [1, '1', 2, 3, 4]

#  访问元素直接修改
a[1] = 'ab'
print(a)  # [1, 'ab', 2, 3, 4]

# 查找元素 （in , not in ,index , count） 查看元素是否存在
if 1 in a:
    print('1在a列表里')

b = [2, 3, 4, 2, 4]
# print(b.index('2',1,3))# 区间内查找左开右闭 找不到报ValueError错误
print(b.index(2, 0, 3))  # 区间内查找左开右闭 # 索引位置0
print(b.count(2))  # 次数2

# 删除元素 （del , pop ,remove）
# del：根据下标进行删除
# pop:删除最后一个元素
# remove：根据元素的值进行删除

del b[0]
print(b)  # [3, 4, 2, 4]
print(b.pop())  # 4 返回被删除的元素
print(b)  # [3, 4, 2]
b.remove(4)
print(b)  # [3, 2]

# 排序（sort,reverse）
# sort默认是从小到大，参数reverse=True 可以从大到小
so = [3, 2, 7, 1, 4, 5]
so.sort()
print(so)  # [1, 2, 3, 4, 5, 7]
so.sort(reverse=True)
print(so)  # [7, 5, 4, 3, 2, 1]

# 列表的嵌套
# lista=[[],[],[]]
# 应用： 8 位老是随机分配三个办公室
import random

# 定义教室
office = [[], [], []]
# 老师
teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for name in teacher:
    index = random.randint(0, 2)  # 三个房间
    office[index].append(name)

# 打印观察
offIn=0
for value in office:
    print('房间%d有%d人'%(offIn+1,len(value)))
    offIn+=1
    print(value)
# 随机结果
# 房间1有5人
# ['a', 'c', 'e', 'g', 'h']
# 房间2有2人
# ['d', 'f']
# 房间3有1人
# ['b']

