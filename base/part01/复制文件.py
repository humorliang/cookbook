# -*- coding:utf-8 -*-
filename = input('请输入您要备份的文件名：')
f = open(filename, 'r')
if f:
    # 查找后缀
    index = filename.rfind('.')
    if index > 0:
        suffix = filename[index:]
        # 定义副本名
        copyFileName = filename[:index]+'副本'+suffix
        fc = open(copyFileName, 'w+')
        # 把旧文件数据一行行写入新文件里
        for lineCon in f.readlines():
            fc.write(lineCon)
        f.close()
        fc.close()
