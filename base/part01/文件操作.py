# -*-coding:utf-8 -*-
# 文件操作
# 文件的打开使用open()函数，文件不存在新建，文件存在则修改
# 文件的访问模式
#  默认       说明
#   r          只读（默认）
#   w         只写，文件存在则覆盖。不存在新建
#   a         追加，
#  rb         二进制格式只读
#  wb         二进制格式只写
#  ab         二进制格式追加
#  r+         打开一个文件用于读写
#  w+         打开一个文件用于读写
#  a+         打开一个文件用于追加
#  rb+         以二进制格式打开一个文件用于读写
#  wb+         以二进制格式打开一个文件用于读写
#  ab+         以二进制格式打开一个文件用于追加

# 打开文件
f = open('test.txt', 'w+')
# 书写文件
f.write('this is a test')
# 读取文件 open不写打开模式 默认从上次位置开始°
# read(num) num表示要读取的字节数，没有则读取全部
r = f.read()
print(r)
f.close()

# readlines(num) num行数 没有时全读 返回一个列表每一行作为一个参数
f2 = open('test2.txt')
con = f2.readlines()
print(con)  # ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5']
f2.close()
