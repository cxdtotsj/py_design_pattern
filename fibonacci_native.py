# -*- coding: utf-8 -*-
# @Data : 2019-11-30

'''
斐波那锲未使用装饰器时的例子

'''

def fibonacci(n):
    assert (n >= 0), 'n muse be >= 0'
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)

# 原始改善代码

known = {0:0, 1:1}

def fibonacci_1(n):
    assert (n >= 0), 'n muse be >= 0'
    if n in known:
        return known[n]
    res = fibonacci_1(n-1) + fibonacci_1(n-2)
    known[n] = res
    return res


if __name__ == "__main__":
    # from timeit import Timer
    # t = Timer('fibonacci_1(8)', 'from __main__ import fibonacci_1')
    # print(t.timeit())

    # fibonacci_1(8)
    fibonacci(8)