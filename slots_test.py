#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午5:37
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''
slots 魔法：限定允许绑定的属性.
__slots__ 设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 slots，
这样，子类允许定义的属性就是自身的 slots 加上父类的 slots。
'''


'''
我们创建了实例 p 之后，给它绑定了一个新的属性 z，这种动态绑定的功能虽然很有用，但它的代价是消耗了更多的内存。
因此，为了不浪费内存，可以使用 __slots__ 来告诉 Python 只给一个固定集合的属性分配空间
'''

class Point(object):
    __slots__ = ('x', 'y')       # 只允许使用 x 和 y

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

if __name__ == "__main__":
    p = Point(3,4)
    p.z = 5
    pass