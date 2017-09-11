#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午5:45
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com


class Foo(object):
    foo = True

class Bar(object):
    bar = True

def echo(cls):
    print cls

def select(name):
    if name == 'foo':
        return Foo        # 返回值是一个类
    if name == 'bar':
        return Bar

if __name__ == "__main__":
    echo(Foo) # 把类作为参数传递给函数 echo
    cls = select('foo')
    print cls