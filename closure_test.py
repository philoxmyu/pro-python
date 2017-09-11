#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午3:56
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''
闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
闭包在运行时可以有多个实例，即使传入的参数相同。
'''

def make_pow(n):
    def inner_func(x):     # 嵌套定义了 inner_func
        return pow(x, n)   # 注意这里引用了外部函数的 n
    return inner_func      # 返回 inner_func

def count():  #尽量避免在闭包中引用循环变量，或者后续会发生变化的变量
    funcs = []
    for i in [1, 2, 3]:
        def f():
            return i
        funcs.append(f)
    return funcs

if __name__ == "__main__":
    pow2 = make_pow(2)
    print pow2(3)