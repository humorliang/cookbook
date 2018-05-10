# coding：utf-8

# 命名空间；所处环境
# 作用域
# globals 、locals
# 经常会提到局部变量和全局变量，之所有称之为局部、全局，就是因为他们的自作用的区域不同，这就是作用域

# LEGB规则
# locals -> enclosing function -> globals -> builtins

# locals，当前所在命名空间（如函数、模块），函数的参数也属于命名空间内的变量

# enclosing，外部嵌套函数的命名空间（闭包中常见）

# globals，全局变量，函数定义所在模块的命名空间

# builtins，内建模块的命名空间。

#   Python 在启动的时候会自动为我们载入很多内建的函数、类，
#   比如 dict，list，type，print，这些都位于 __builtin__ 模块中，
#   可以使用 dir(__builtin__) 来查看。
#   这也是为什么我们在没有 import任何模块的情况下，
#   就能使用这么多丰富的函数和功能了。

#   在Python中，有一个内建模块，该模块中有一些常用函数
#   在Python启动后，
#   且没有执行程序员所写的任何代码前，Python会首先加载该内建函数到内存。
#   另外，该内建模块中的功能可以直接使用，不用在其前添加内建模块前缀，
#   其原因是对函数、变量、类等标识符的查找是按LEGB法则，其中B即代表内建模块
#   比如：内建模块中有一个abs()函数，其功能求绝对值，如abs(-20)将返回20。

a = 'globals'


def fun():
    a = 'enclosing'

    def fun_in():
        a = 'local'
        print(a)  # local
    fun_in()
    print(a)  # enclosing


fun()
print(a)  # globals
print(str)  # <class 'str'> 内建的
# 查看内建函数
print(dir(__builtins__))
