#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午4:37
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''
类方法使用 @classmethod 装饰器，可以使用类（也可使用实例）来调用方法。
静态方法使用 @staticmethod 装饰器，它是跟类有关系但在运行时又不需要实例和类参与的方法，可以使用类和实例来调用。
'''

class A(object):
    bar = 1
    @classmethod
    def class_foo(cls):
        print 'Hello, ', cls
        print cls.bar

    @staticmethod
    def static_foo():
        print 'Hello, ', A.bar

if __name__ == "__main__":
    A.class_foo()
    A.static_foo()