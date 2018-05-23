# coding:utf-8
# 多平台进程编程
from multiprocessing import Process
import os

# 子进程要执行的代码
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

def run_proc():
    print('子进程在运行,pid=%d...' % os.getpid())


if __name__ == '__main__':
    print('父进程%d' % os.getpid())
    p = Process(target=run_proc)
    p.start()
    p.join()
