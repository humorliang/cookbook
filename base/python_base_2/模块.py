# -*-coding:utf-8 -*-
# 模块
# 含有一定功能的函数类工具包

# import 方式导入
# import moudle1,moudel2...
# 调用的时候
# 模块名.函数名
import math
# 调用
print(math.sqrt(2))  # 1.4142135623730951

# from...import...方式导入
# Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
# 我们只需要某个函数的时候就这样调用，还可以引入一些全局变量、类等
# from 模块名 import 函数1，函数2...

# from … import * 导入全部

# as 将导入的部分起别名

# 定位模式
# 当你导入一个模块，Python解析器对模块位置的搜索顺序是：

# 1.当前目录
# 2.如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
# 3.如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
# 4.模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。


# 模块的制作
# 定义自己的模块
# 每个Python文件都可以作为一个模块，模块的名字就是 文件的名字。

# 调用直接导入模块就可以调用

# 自定义模块测试
# __name__变量在执行该文件 时为  __main__ 在导入的时候  为模块名

# 导入时的__name__
# import module  # __name__为： module


# 模块中的__all__变量决定哪些在使用from..import * 导入
from module import *
# 在模块中__all__变量没有add所以按*导入会出错
# print(add(1, 2))  # NameError: name 'add' is not defined
