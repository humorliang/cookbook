# -*-coding:utf-8 -*-
#  文件操作
import os

# 重命名
# os.rename('test.txt','test重命名后.txt')

# 删除文件
# os.remove('del.txt')

# 创建文件夹
# os.mkdir('python创建的')

# 获取当前目录
print(os.getcwd())  # e:\work\python\cookbook\base\part01

# 改变默认（当前）目录
print(os.chdir('../'))  # none
print(os.getcwd())  # e: \work\python\cookbook\base

# 获取当前目录列表
print(os.listdir('./'))  # 当前目录已更改 ['base.py', 'part01']

# os.chdir('./part01')
# 删除文件夹
# os.rmdir('python创建的')
