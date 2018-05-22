# /usr/lib/python3

# 多进程修改全局变量，多进程中每个进程都有一份全局变量
# 互不影响

import os
import time

pid = os.fork()
num = 0
if pid == 0:
    num += 1
    print('嘿嘿1---num=%d' % num)
else:
    time.sleep(1)
    num += 1
    print('嘿嘿2---num=%d' % num)
