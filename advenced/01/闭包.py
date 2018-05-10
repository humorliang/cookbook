# coding:utf-8
# 闭包
# 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
# 内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。


def test(num):

    def test_in(num_in):
        print('test_in函数，num_in是%d' % num_in)
        return num+num_in

    # test返回一个函数的引用 ，返回的就是闭包
    return test_in


# 这里的参数2 就是num
add = test(2)

# 这里的参数 10 就是 num_in
print(add(10))
# test_in函数，num_in是10
# 12

# 线性方程的案例


def line_fun(a, b):
    def line(x):
        return a*x+b
    return line


lin1 = line_fun(1, 3)
lin2 = line_fun(2, 3)

print(lin1(2))  # 5
print(lin2(2))  # 7

# 闭包思考：
# 闭包也具有提高代码可复用性的作用
# 1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
# 2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
