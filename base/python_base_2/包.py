# coding:utf-8
# 一个文件夹含有一个__init__.py的文件就是一个包
# 其他py文件就是包内的模块

# 还可以嵌套包

# __init__.py文件的作用

# 1.__init__为空
# 仅仅把这个包导入，不会导入包的模块

# 2. __init__.py定义了一个__all__变量 控制着from 包名 import * 时的模块

# __init__.py文件中的内容包导入时会被执行
# from package import * #package--init

# 有__all__变量
# from package import *
# package--init
# package--a
# package--b
