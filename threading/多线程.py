# coding:utf-8
# 多线程-threading
# 可以明显看出使用了多线程并发的操作，花费时间要短很多
# 创建好的线程，需要调用start()方法来启动
import threading
from time import sleep, ctime


def sayLove():
    print('this is love')
    sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=sayLove)
        t.start()


