#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午4:41
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com
'''
常用的特殊方法：
__new__
__str__ , __repr__
__iter__
__getitem__ , __setitem__ , __delitem__
__getattr__ , __setattr__ , __delattr__
__call__

__new__ 在 __init__ 之前被调用，用来创建实例。
__str__ 是用 print 和 str 显示的结果，__repr__ 是直接显示的结果。
__getitem__ 用类似 obj[key] 的方式对对象进行取值
__getattr__ 用于获取不存在的属性 obj.attr
__call__ 使得可以对实例进行调用

'''


'''
关于 __new__ 和 __init__ 有几点需要注意：
__new__ 是在 __init__ 之前被调用的；
__new__ 是类方法，__init__ 是实例方法；
重载 __new__ 方法，需要返回类的实例；
'''
class A(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print "EXISTS", cls
            return A._dict['key']
        else:
            print "NEW"
            obj = object.__new__(cls)
            print obj
            return obj

    def __init__(self):
        print "INIT", self
        A._dict['key'] = self

'''
str & repr
'''
class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Foo object (name: %s)' % self.name

    __repr__ = __str__

'''
iter &  getitem
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 返回迭代器对象本身
        return self

    def next(self):      # 返回容器下一个元素
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in xrange(n):
            a, b = b, a + b
        return a

'''
我们一般使用 obj.method() 来调用对象的方法，那能不能直接在实例本身上调用呢？在 Python 中，只要我们在类中定义 __call__ 方法，就可以对实例进行调用
'''
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __call__(self, z):
        return self.x + self.y + z

if __name__ == "__main__":
    a1 = A()
    a2 = A()
    print type(A), type(a1)

    a = Foo("aa")
    print a
    fib = Fib()
    for i in fib:
        if i > 10:
            break
        print i
    print "getitem", fib[3]

    p = Point(3,4)
    print callable(p)
    print p(6)