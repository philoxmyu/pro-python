#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午4:00
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''

本质上，装饰器就是一个返回函数的高阶函数。
装饰器可以动态地修改一个类或函数的功能，通过在原有的类或者函数上包裹一层修饰类或修饰函数实现。
事实上，装饰器就是闭包的一种应用，但它比较特别，接收被装饰函数为参数，并返回一个函数，赋给被装饰函数，闭包则没这种限制。

装饰器可以定义多个，离函数定义最近的装饰器先被调用
@decorator_one
@decorator_two
def func():
    pass  ====> func = decorator_one(decorator_two(func))
'''

def hello():
    return 'hello world'

def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

'''
对带参数的函数进行装饰
内嵌包装函数的参数传给了func，即被装饰函数，也就是说内嵌包装函数的参数跟被装饰函数的参数对应，这里使用了 (*args, **kwargs)，是为了适应可变参数。
'''
def makeitalic2(func):
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '<i>' + ret + '</i>'
    return wrapped

@makeitalic2
def hello2(name1, name2):
    return 'hello %s, %s' % (name1, name2)


'''
带参数的装饰器：其实就是在装饰器外面多了一层包装，根据不同的参数返回不同的装饰器
'''
def wrap_in_tag(tag):
    def decorator(func):
        def wrapped(*args, **kwargs):
            ret = func(*args, **kwargs)
            return '<' + tag + '>' + ret + '</' + tag + '>'
        return wrapped

    return decorator
'''
makebold = wrap_in_tag('b') #根据'b'返回 makebold 生成器
@makebold
def hello3(name):
    return 'hello %s' % name
'''

@wrap_in_tag('b')
def hello3(name):
    return 'hello %s' % name


'''
多个装饰器
'''
def makebold(func):
    def wrapped():
        return '<b>' + func() + '</b>'
    return wrapped

def makeitalic2(func):
    def wrapped():
        return '<i>' + func() + '</i>'
    return wrapped

@makebold
@makeitalic2
def hello4():
    return 'hello world'

'''
基于类的装饰器
__init__()：它接收一个函数作为参数，也就是被装饰的函数
__call__()：让类对象可调用，就像函数调用一样，在调用被装饰函数时被调用
'''
class Bold(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return '<b>' + self.func(*args, **kwargs) + '</b>'

@Bold
def hello5(name):
    return 'hello %s' % name


'''
类装饰器带参数
'''
class Tag(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            return "<{tag}>{res}</{tag}>".format(
                res=func(*args, **kwargs), tag=self.tag
            )
        return wrapped

@Tag('b')
def hello6(name):
    return 'hello %s' % name


'''
前面提到，使用装饰器有一个瑕疵，就是被装饰的函数，它的函数名称已经不是原来的名称了
为了消除这样的副作用，Python 中的 functools 包提供了一个 wraps 的装饰器：
'''
from functools import wraps
def makeitalic3(func):
    @wraps(func)       # 加上 wraps 装饰器
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeitalic3
def hello7():
    return 'hello world'

if __name__ == "__main__":
    hello = makeitalic(hello)
    print hello()
    print hello.__name__     # wrapped

    print hello2("s1", "s2")  # 对带参数的函数进行装饰
    print hello3("s3")  # 带参数的装饰器
    print hello4()  # 多个装饰器
    print hello5('s5')  # 类装饰器
    print hello6('s6') # 带参数的类装饰器
    print hello7() # functools.wraps