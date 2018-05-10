# coding:utf-8
# import 搜索路径
import sys
# sys.path.insert(0, 'path')  在程序执行时导入模块路径
print(sys.path)
# ['path',
# 'e:\\work\\python\\cookbook\\advenced\\02',
#  'D:\\Python\\Python35\\lib\\site-packages\\pip-10.0.0-py3.5.egg',
#  'D:\\Python\\Python35\\python35.zip',
#     'D:\\Python\\Python35\\DLLs',
#     'D:\\Python\\Python35\\lib',
#     'D:\\Python\\Python35',
#      'D:\\Python\\Python35\\lib\\site-packages']

# 模块一旦导入 不能再导入，要用reload(模块)

# 循环导入
# 模块 a 导入模块 b 但是模块 b 中又导入模块 a
# 怎样避免循环导入
# 程序设计上分层，降低耦合
# 导入语句放在后面需要导入时再导入，例如放在函数体内导入
