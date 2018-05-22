# coding:utf-8
# threading模块中定义了Lock类，可以方便的处理锁定：

# #创建锁
# mutex = threading.Lock()
# #锁定
# mutex.acquire([blocking])
# #释放
# mutex.release()
# 其中，锁定方法acquire可以有一个blocking参数。

# 如果设定blocking为True，则当前线程会堵塞，直到获取到这个锁为止（如果没有指定，那么默认为True）
# 如果设定blocking为False，则当前线程不会堵塞

from threading import Thread, Lock
import time


# 创建互斥锁
mutex = Lock()
g_num = 0


def test1():
    global g_num
    # true 为堵塞
    # flase 为非堵塞
    for i in range(100000):
        mutexFlag = mutex.acquire(True)  # 上锁
        if mutexFlag:
            g_num += 1
            mutex.release()  # 释放锁
    print('test1 g_num%d' % g_num)


def test2():
    global g_num
    # true 为堵塞
    # flase 为非堵塞
    for i in range(100000):
        mutexFlag = mutex.acquire(True)  # 上锁
        if mutexFlag:
            g_num += 1
            mutex.release()  # 释放锁
    print('test2 g_num%d' % g_num)


p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print('----g_num--%d' % g_num) # 主线程
