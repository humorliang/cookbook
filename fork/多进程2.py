# /usr/lib/python3
# getpid() 和 getppid()获得父子进程的id
import os

rpid = os.fork()  # fork()函数调用一次返回两次
# 子进程永远返回0，父进程返回子进程的id

if rpid < 0:
    print("fork调用失败")
elif rpid == 0:
    print('我是子进程（%s）我的父进程(%s)' % (os.getpid(), os.getppid()))
else:
    print('我是父进程（%s）我的子进程(%s)' % (os.getpid(), rpid))

print('父子进程都可执行这里代码')
