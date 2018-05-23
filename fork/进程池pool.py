# coding:utf-8
# 当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，
# 但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法
from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print('任务%s开始执行，进程号为%d' % (msg, os.getpid()))
    time.sleep(random.randint(1, 3))
    t_stop = time.time()
    print(msg, '执行完毕耗时%0.2f' % (t_stop-t_start))


# 进程池最大线程数
po = Pool(3)
for i in range(5):
    # 定义任务数5个
    po.apply_async(worker, (i,))  # 参数为元组一个元素不能缺少 , 号


po.close()  # 关闭进程池，不再接受新的进程任务
po.join()  # 主进程等子进程结束再结束
