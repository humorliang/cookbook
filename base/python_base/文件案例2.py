# -*-coding：utf-8 -*-

# 制作文件密码本
print('----------------')
print('---1.查询密码----')
print('---2.删除密码----')
print('---3.存储密码----')
print('---4.更改密码----')
print('---5.退出----')
print('----------------')


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
    while True:
        row=f.readline()
        if len(row)==0:
            break
        else:
            acountList=row.split(':')
            if acountList[0]=='www.baidu1.com':
                userList.append(acountList[0]+':'+'2222'+'\n')
            else:
                userList.append(row)
print(type(userList)) # list
print(len(userList)) # 1
for row2 in userList:
    print(row2)
with open('pwd2.txt','w') as f:
    for row in userList:
        f.write(row)