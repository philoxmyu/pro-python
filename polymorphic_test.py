#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午4:34
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''
多态的概念其实不难理解，它是指对不同类型的变量进行相同的操作，它会根据对象（或类）类型的不同而表现出不同的行为。
有了继承，才有了多态，不同类的对象对同一消息会作出不同的相应
'''

class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print 'Hello, I am %s.' % self.name

class Dog(Animal):
    def greet(self):
        print 'WangWang.., I am %s.' % self.name

class Cat(Animal):
    def greet(self):
        print 'MiaoMiao.., I am %s' % self.name

def hello(animal):
    animal.greet()


if __name__ == "__main__":
    dog = Dog('dog')
    hello(dog)

    cat = Cat('cat')
    hello(cat)
