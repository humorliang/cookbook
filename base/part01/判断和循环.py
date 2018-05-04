# -*-coding:utf-8-*-

# if-else
knife = 10  # 刀
if knife > 10:
    print('不能上火车')
else:
    print('可以上火车')

# else if
score = 80
if score >= 60 and score < 80:
    print('成绩合格 等级B')
elif score >= 80:
    print('等级A')
elif score < 60:
    print('不及格')

# if嵌套
num = 30
if num > 10:
    if num > 20:
        print('num大于20')
    else:
        print('num小于20大于10')
else:
    print('num小于10')

# while 循环应用
i = 1
while i < 10:
    print('i为%d' % i)
    i += 1

# 计算1~100的累计和
ii = 1
sum = 0
while ii <= 100:
    sum = sum+ii
    ii += 1
print('1~100的累计和：%d' % sum)

# 计算1~100的偶数累计和
i3 = 1
sum2 = 0
while i3 <= 100:
    if i3 % 2 == 0:
        sum2 = sum2+i3
        i3 += 1
    i3 += 1
print('1~100的累计和：%d' % sum2)

# while 的嵌套应用
row = 1
while row <= 6:
    col = 1
    while col <= row:
        print('*', end='')  # print结尾默认是换行符，可以用end参数指定
        col += 1
    print('\n')
    row += 1

# 九九乘法表
r = 1
while r <= 9:
    c = 1
    while c <= r:
        print('%d*%d=%d\t' % (c, r, c*r), end='')
        c += 1
    print('\n')
    r += 1

# for循环 for循环可以遍历任何序列对象 字符串 列表
string = 'love'
li = [1, 2]
for i in string:
    print(i)
print('------------')
for value in li:
    print(value)
print('--------------')
# 配合else做没有数据
list1 = []
for value in list1:
    print(value)
else:
    print('没有数据')

# break 和continue
# breek 用于结束整个循环  continue 用于结束本次循环
# break/continue只会在最近的一层循环中起作用，只能用在循环中
m = 0
while True:
    m += 1
    if m > 3:
        print('break')
        break
    print('m:%d' % m)

n = 0
while n < 5:
    n += 1
    if n == 3:
        print('continue')
        continue
    print('n：%d' % n)

# 小结：if while for 可以随意组合