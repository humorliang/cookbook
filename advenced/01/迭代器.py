# coding:utf-8
# 迭代器
# 迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。

# 可迭代对象
# 以直接作用于 for 循环的数据类型有以下几种：
# 一类是集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等；
# 一类是 generator ，包括生成器和带 yield 的generator function。
# 这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable 。

# 判断可迭代
# isinstance() 判断对象是否可 Iterable对象：

# 内建集合模块，提供许多的集合类
from collections import Iterable, Iterator

print(isinstance([], Iterable))  # True

# 迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 判断是迭代对象
# 可以使用 isinstance() 判断一个对象是否是 Iterator 对象
print(isinstance((x for x in range(10)), Iterator))  # true

# iter()函数
# 生成器都是 Iterator 对象，但 list 、 dict 、 str 虽然是 Iterable ，却不是 Iterator 。
# 把 list 、 dict 、 str 等 Iterable 变成 Iterator 可以使用 iter() 函数：
print(isinstance([], Iterator))  # False 可迭代但不是迭代对象

print(isinstance(iter([]), Iterator)) # True

# 小结
# 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 凡是可作用于 next() 函数的对象都是 Iterator 类型
# 集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。
