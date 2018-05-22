# /usr/lib/python3

import os

#  fork函数，只能在unix/linux/mac上运行，windows不可以
# 程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），然后复制父进程的所有信息到子进程中
# 然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中是子进程的 id号
pid = os.fork()
if pid == 0:
    print('汉哈哈')
else:
    print('nohaha')

 
