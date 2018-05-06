# -*-coding:utf-8-*-
# 引用
# 在python中一切都是对象，可以看作对地址的引用
# 在python中可以用id()来判断两个变量是否相等
a = '1'
b = a
print(id(a))  # 1400832914744 可以看作内存地址
print(id(b))  # 1400832914744

# 小案例
# 案例 1：对一个纯数字的列表进行，求最大值和最小值
# 案例 2：统计字符串中各字符的个数
# 案例 3：实现一个完整的目录的组装
print('-----demo1-----')
a_list = [1, 3, 2, 4, 6, 5]
max_num = a_list[0]
min_num = a_list[0]
for num in a_list:
    if num > max_num:
        max_num = num
    elif num < min_num:
        mn_num = num
print('最大值：%d,最小值：%d' % (max_num, min_num))  # 最大值：6,最小值：1
print('-----end----')
print('-----demo2-----')
a_str = 'thisisastring'
a_dict = {}
for aStr in a_str:
    a_dict[aStr] = int(a_dict.get(aStr, 0))+1  # get方法设置默认值
print(a_dict)
# {'h': 1, 'n': 1, 'a': 1, 't': 2, 'i': 3, 'r': 1, 's': 3, 'g': 1}
print('----end-----')
print('-----demo3-----')
pList = ['home', 'info', 'ba']
pStr = '/' # 指定字符连接的字符串
print(pStr.join(pList))  # home/info/ba
print('------------')
