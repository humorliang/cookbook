# coding:utf-8
# 线程代码的封装，自定义一个新的子类，继承threading.Thread就可以了
# 然后重写run方法

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = '我是'+self.name+':'+str(i)
            print(msg)


# if __name__ == '__main__':
#     t = MyThread()
#     t.start()


# 县城的执行顺序是不确定的
def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()
