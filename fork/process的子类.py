# coding:utf-8
from multiprocessing import Process
import os
import time

# 自定义线程类
# 实例化自定义类时相当于创建一个线程类


class MyProcess(Process):
    '''自定义线程类'''
    # 父类初始化

    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    # 重写run方法
    def run(self):
        print('子进程pid=%s,父进程pid=%s' % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_over = time.time()
        print('(%s)执行结束，耗时%0.2f秒' % (os.getpid(), t_over-t_start))


if __name__ == '__main__':
    t_start = time.time()
    p = MyProcess(2)
    # 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法，所以这里会执行p1.run()
    p.start()
    p.join()
    t_stop = time.time()
    print('(%s)执行结束，耗时%0.2f' % (os.getpid(), t_stop-t_start))
