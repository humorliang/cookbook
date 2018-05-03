# -*- coding:utf-8 -*-

# 这是注释

# 变量以及类型

# 变量名：字母数字下划线组成
num = 10  # 这是一个变量

# 类型
# 1. Number数字：int float long complex
# 2. 布尔类型： True False
# 3. String 字符串
# 4. List 列表
# 5. Tuple 元组
# 6. Dictionary 字典

# 标识符和关键字
# 标识符是自己定义的：由字母和下划线数字组成，区分大小写
# 见名知意 ：小驼峰 userName  大驼峰 UserName  下换线 user_name

# 关键字 ： 有特殊功能的标识符
import keyword

print(keyword.kwlist)  # 输出所有的关键字

# 输出
# 普通输出
print('普通输出')

# 格式化输出
age = 10
name = 'xiaohu'
print('姓名%s,年龄%d' % (name, age))

# 常用格式符号
# %c (字符) %s (通过str()字符串进行转换来格式化)
# %s %i %d %u %o %x %X %e %E %f %g %G

# 转义自符 \n \t

# 输入
# info = raw_input("提示信息")
# print(help(raw_input)) py3不支持raw_input()

# a=10
# info = input()  # 只接受接受表达式 字符串要使用‘’不然会当成变量复制给左边
# print(info) # 把表达式的结果赋值给左边


# 用算符
# 算术用算符
# + 加 - 减  *乘  /除 //取整除 %取余 **幂

# 赋值
# =
# 复合赋值运算
# += 加法赋值  c+=a c=c+a  -= *= /= %= **= //=

# 常用的数据类型转换
# print(help(int))
# int(x[,base]) 将x转换为整型
# long(x[,base]) 将x转换为长整形
# float(x) 将x转换为一个浮点数
# complex(real[,imag]) 创建一个复数
# str(x) 将对象x转换为字符串
# repr(x) 将对象x转为表达式字符串
# eval(str) 计算str中有效的表达式并返回一个对象
# tuple(s) 将序列s转化为一个元组
# list(s) 将序列s转化为一个列表
# chr(x) 将整数转换为一个字符
# unich(x) 将整数转换为Unicode字符
# ord(x) 将一个字符转换为他的整数值
# hex(x) 将一个整数转换为它的十六进制字符串
# oct(x) 将一个整数转换为一个八进制字符串


