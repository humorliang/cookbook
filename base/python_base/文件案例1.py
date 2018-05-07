# -*- coding:utf-8 -*-
# 读取文件，显示除 # 号开头的所有行

# 存储容器
lineList=[]
#打开文件
with open('file1.txt') as f:
    # 对文件进行一行行读写
    for lineData in f.readlines():
        if not lineData.startswith('#'):
            lineList.append(lineData)
# ['this is show line\n', 'this is show line2\n', 'this is show line3\n', '\n']
print(lineList)
