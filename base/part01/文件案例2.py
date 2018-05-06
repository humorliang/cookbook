# -*-coding：utf-8 -*-

# 制作文件密码本
print('----------------')
print('---1.查询密码----')
print('---2.删除密码----')
print('---3.存储密码----')
print('---4.更改密码----')
print('---5.退出----')
print('----------------')

# while True:
#     funNum = input('请输入功能序号：')
#     if funNum == 1:
#         name = input('请输入帐户名：')
#         with open('pwdBook.txt') as f:
#             for line in f.readlines():
#                 row = line.split(':')
#                 if row[0] == name:
#                     print('账户：%s;密码：%s', (row[0], row[1]))
#                 else:
#                     print('没有查询到')
#     elif funNum==2:
#         name = input('请输入帐户名：')
#         with open('pwdBook.txt') as f:
#             for line in f.readlines():
#                 row = line.split(':')
#                 if row[0] == name:
#                     print('账户：%s;密码：%s', (row[0], row[1]))
#                 else:
#                     print('没有查询到')

# 打开文件
# 写入
# with open('pwdBook.txt','w+') as f:
#     name_pwd='www.baidu.com:12345\n'
#     f.writelines(name_pwd)
#     name_pwd2 = 'www.baidu2.com:12345\n'
#     f.writelines(name_pwd2)

# 读取
# with open('pwdBook.txt', 'r') as f:
#     for line in f.readlines():
#         row=line.split(':')
#         print(row)

# 修改
userList = []
with open('pwdBook.txt', 'r+') as f:
    for line in f.readlines():
        row = line.split(':')
        if row[0] == 'www.baidu2.com':
            row[1] = '33333'

            userList.append(row[0]+':'+row[1]+'\n')
        else:
            userList.append(line)

print(' '.join(userList))
with open('pwdBook.txt', 'w') as f:
    f.write(''.join(userList))
