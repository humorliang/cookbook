# -*-coding:utf-8-*-
# 字符串的介绍

# 用 ‘’ 或 “ ” 或 ‘‘‘ ’’’表示的都是字符串
s = 'hello string'
print('我是字符串:%s' % s)

# input 获取的数据都是字符串

# 下标和切片
# 下标索引
# 字符串中的下表索引，右索引从0开始,左索引从-1开始
print('-----------------')
print(' a  b  c  d  e  f')
print(' ↑  ↑  ↑  ↑  ↑  ↑')
print(' 0  1  2  3  4  5')
print('-6 -5 -4 -3 -2 -1')
print('-----------------')

# 下表可以访问字符
name = 'xiaomin'
print(name[0])  # x
print(name[-1])  # n

# 切片 ：截取对象的一部分 。列表，字符串，元组都支持
# 语法：[起始：结束：步长] # 结束是不包括结束下标的元素
print(name[0:2])  # xi
print(type(name[0:2]))  # str

# 终止不写默认为到最后
print(name[2:])  # aomin
# 开头步长不写默认为左索引开头,
print(name[:2])  # xi
# 不指定开头步长为负数时从右索引开始
print(name[:2:-1])  # nimo

# 开始、结束、步长下标都可以用负数表示
print(name[0:-1])  # xiaomi
print(name[:-5:-1])  # nimo

# 小案例，字符串的反转
aStr = 'love'
print(aStr[::-1])  # evol


# 字符串的常见操作

# find 查找mystr是否包含str 找到返回str的首字母索引 str看成为一个整体
# 未找到返回 -1 ; 用法：mystr.find(str,start=0,end=len(mystr))
mystr = 'i love u and u'
print(mystr.find('u'))  # 7 # 只会返回第一个找到的

# index 与find方法类似 但 未找到的时候 会报valueError 异常
# print(mystr.index('you'))  # ValueError: substring not found
print(mystr.index('u'))  # 7

# count 返回str在开始和结束之间 在mystr出现的次数
print(mystr.count('u'))  # 2
print(mystr.count('u', 8, len(mystr)))  # 1 该函数不接受关键字参数，只能用占位

# replace 把mystr 中的 str1 替换成 str2 如果count 指定替换不超过count次
mystr.replace('u', 'U', mystr.count('u'))  # 重新生成一个字符串返回，不会改原有的
print(mystr)  # i love u and u
print(mystr.replace('u', 'U', mystr.count('u')))  # i love U and U

# split 以str作为分隔符 对mystr进行切片 ，如果maxsplit有指定 作为分割的次数
# 简单的理解为砍几次
word = mystr.split(' ')
word2 = mystr.split(' ', 2)
print(word)  # ['i', 'love', 'u', 'and', 'u']
print(word2)  # ['i', 'love', 'u and u']

# capitalize 使字符串第一个字母大写
print(mystr.capitalize())  # I love u and u

# title 使字符串的每个单词首字母大写
print(mystr.title())  # I Love U And U

# startswith 检查字符串是否以str开头 是返回 true 否则 false
print(mystr.startswith('i'))  # True

# endswith 检查字符串是否以str结尾 是true 否 false
print(mystr.endswith('u'))  # True

# lower 将mystr所有字符串转换为小写
MyStr = 'LOVE'
print(MyStr.lower())  # love

# mystr.upper() 小写变大写

# mystr.ljust(with) 左对齐使用空格填充至长度with的新字符串
# mystr.rjust(with) 右对齐....
# mystr,center(with) 居中对齐 .....

# mystr.lstrip() 删除字符串左边的空白字符
# mystr.rstrip() .........右边...
# mystr.strip() 删除两边空白
print('\t uu\n'.strip()) # 'uu'

# mystr.rfind() 右边开始查找
# mystr.rindex() 右边开始查找 异常区别

#  mystr.partition(str) 把mystr以str分割成三部分 str前 str str后 
print(type(mystr.partition('u')))  # ('i love ', 'u', ' and u') #tuple
# mystr.rpartition(str) 右边开始

# mystr.splitlines() 按行进行分割 返回各行元素做列表
# mystr.isalpha() 检查是否都是字母 是True 否 false
# mystr.isdigit() 检查是否都是数字 是True 否 false
# mystr.isalnum() 所有字符都是字母或数字则返回True 否False
# mystr.isspace() 只包含空格 返回True 否false

# join mystr每个字符后面插入str,构造出新字符串
Str=' '
list_=['i','love','u']
print(Str.join(list_))  # i love u


# 小案例： 给定一个字符串 返回使用空格或者 ’\t‘分割后的倒数第二个子串
testStr='ni hao a \n this is \t a test \t you can solve\t a problem'
print(testStr.split(' '))
#['ni', 'hao', 'a', '\n', 'this', 'is', '\t', 'a', 'test', '\t', 'you', 'can', 'solve\t', 'a', 'problem']
print(testStr.split('\t'))
# ['ni hao a \n this is ', ' a test ', ' you can solve', ' a problem']
print(testStr.split())  # str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
#['ni', 'hao', 'a', 'this', 'is', 'a', 'test', 'you', 'can', 'solve', 'a', 'problem']
