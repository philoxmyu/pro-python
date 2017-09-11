#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午1:56
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''

__new__ 方法创建实例对象供__init__ 方法使用，__init__方法定制实例对象
__new__ 方法必须返回值，__init__方法不需要返回值

'''


class Foo(object):

    #price = 50

    def __init__(self, price=50):
        self.price = price

    def __new__(cls, *args, **kwds):
        print cls, type(cls)
        inst = object.__new__(cls, *args, **kwds)
        print(inst)
        return inst

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

class PositiveInteger(int):

    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))


class PositiveInteger2(int):
    def __new__(cls, value):
        return super(PositiveInteger2, cls).__new__(cls, abs(value))



class Singleton(object):
    '''
    __new__ 实现单例
    '''
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

if __name__ == "__main__":
    foo = Foo()
    print(foo.how_much_of_book(8))
    print(dir(Foo))

    i = PositiveInteger(-3)
    print i

    j = PositiveInteger2(-3)
    print j