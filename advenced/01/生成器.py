# coding:utf-8
# 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 创建生成器的方法1:
# 只要把一个列表生成式的 [ ] 改成 ( )
g = (x for x in range(5))
print(g)  # <generator object <genexpr> at 0x00000256ED4C97D8>
# 可以通过 next() 函数获得生成器的下一个返回值
print(next(g))  # 0
print('---------')
for x in g:
    print(x)
# 1 2 3 4
print('-------')
# 创建生成器方法2：使用yield


def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'


# 创建一个生成器对象
g2 = fib(4)

# 可以使用
print(next(g2))  # 1
print(next(g2))  # 1

# 还可以使用
print(g2.__next__())  # 2
print('-----------')


# send() 函数给下一次生成器传值 并返回一个生成器的值


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('上一次迭代器传进来的值：', temp)
        i += 1


# 定义一个生成器对象
g3 = gen()

print(g3.__next__())
# 0
print(g3.__next__())
# 上一次迭代器传进来的值： None
# 1
print(g3.send('mm'))
# 上一次迭代器传进来的值： mm
# 2
print(g3.__next__())
# 上一次迭代器传进来的值： None
# 3
# 总结
# 生成器是这样一个函数，它记住上一次返回时在函数体中的位置。对生成器函数的第二次（或第 n 次）调用跳转至该函数中间，而上次调用的所有局部变量都保持不变。

# 生成器不仅“记住”了它数据状态；生成器还“记住”了它在流控制构造（在命令式编程中，这种构造不只是数据值）中的位置。
# 特点：
# 1.节约内存
# 2.迭代到下一次的调用时，所使用的参数都是第一次所保留下的，即是说，在整个所有函数调用的参数都是第一次所调用时保留的，而不是新创建的
