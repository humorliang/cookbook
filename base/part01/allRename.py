# -*-coding:utf-8 -*-
# 批量改文件名字

import os

# 获取所有的文件名字
# 要切换到修改目录不然无法找文件 
# 程序运行目录与修改的文件不是一级会出现找不到文件异常
os.chdir('./批量改名字/')
nameList = os.listdir()
# print(nameList)
for filename in nameList:
    # print(type(filename))
    os.rename(filename, '批量修改文件名'+filename)
