# coding:utf-8
import functools
print(dir(functools))

# 工具函数
['MappingProxyType', 'RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'WeakKeyDictionary',
 '_CacheInfo', '_HashedSeq', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__', '_c3_merge', '_c3_mro', '_compose_mro',
 '_convert', '_find_impl', '_ge_from_gt', '_ge_from_le', '_ge_from_lt', '_gt_from_ge',
 '_gt_from_le', '_gt_from_lt', '_le_from_ge', '_le_from_gt', '_le_from_lt', '_lru_cache_wrapper',
 '_lt_from_ge', '_lt_from_gt', '_lt_from_le', '_make_key', 'cmp_to_key',
 'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod',
 'reduce', 'singledispatch', 'total_ordering', 'update_wrapper', 'wraps']

# partial函数
# 把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单。


def show(*args, **kwargs):
    print(args)
    print(kwargs)


p1 = functools.partial(show, 1, 2, 3)
p1()  # (1, 2, 3)  {}
p1(4, 5, 6)  # (1, 2, 3, 4, 5, 6) {}

# wraps函数
# 使用装饰器时，有一些细节需要被注意。例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。

# 添加后由于函数名和函数的doc发生了改变，对测试结果有一些影响


def note(func):
    @functools.wraps(func)
    def wrapper():
        '''wrapper function'''
        print('note sommthing')
        return func()
    return wrapper


@note
def test():
    '''test function'''
    print('test')


test()
print(test.__doc__)
# note sommthing
# test
# test function
