#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午3:18
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''
事实上，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。
'''

class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print 'Hello, I am %s.' % self.name


class Dog(Animal):
    def greet(self):
        super(Dog, self).greet()   # Python3 可使用 super().greet()
        print 'WangWang...'

'''
MRO: method resolution order
'''
class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"

class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"

class B(Base):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"

class C(A, B):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"


def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]

if __name__ == "__main__":
    # dog = Dog("dog1")
    # dog.greet()
    c = C()
    print C.__mro__