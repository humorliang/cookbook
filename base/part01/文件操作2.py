# -*-coding:utf-8 -*-
# 获取当前读写的位置 tell()
f = open('test2.txt', 'r')
raed = f.read(2)
print('读取的的数据:', raed)

# 查找当前的位置
pos = f.tell()
print('当前文件位置：', pos)

raed = f.read(2)
print('读取的的数据:', raed)

# 查找当前的位置
pos = f.tell()
print('当前文件位置：', pos)

f.close()
# 读取的的数据: li
# 当前文件位置： 2
# 读取的的数据: ne
# 当前文件位置： 4

print('-------')
# 定位到某个位置seek(offset,from)
# offset: 偏移量 字节   from:方向 0 表示文件开头 1 当前位置 2文件末尾
with open('test2.txt') as f:
    data = f.read(3)
    print('读取的数据：', data)
    # 读取的数据： lin
    pos = f.tell()
    print('当前的位置：', pos)
    # 当前的位置： 3
    # 重新设置位置
    f.seek(4, 0)
    pos = f.tell()
    print('当前的位置：', pos)
    # 当前的位置： 4
print('------')
# 设定位置的时候要用二进制形式打开，不然只能从开头进行读写
# io.UnsupportedOperation: can't do nonzero end-relative seeks
with open('test2.txt', 'rb') as f:
    # 设置文件结尾5字节处
    pos = f.tell()
    print('当前的位置：', pos)
    f.seek(-2, 2)
    # help(f.seek)
    pos = f.tell()
    print('当前的位置：', pos)  # 当前的位置： 31
    overData = f.read()
    print('最后两个数据：', overData)  # 最后两个数据： b'e5'

