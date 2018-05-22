# coding:utf-8
from threading import Thread
import time

# 在一个进程内的所有线程共享全局变量，能够在不适用其他方式的前提下完成多线程之间的数据共享（这点要比多进程要好）
# 缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全

g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print('in--work1,g_num is %d' % g_num)


def work2():
    global g_num
    print('in--work2,g_num is %d' % g_num)


print('in---创建线程之前%d' % g_num)
t1 = Thread(target=work1)
t1.start()

# 延迟保证 t1线程完成
time.sleep(1)

t2 = Thread(target=work2)
t2.start()
