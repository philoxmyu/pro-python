#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午3:28
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com

'''
 把方法『变成』了属性
'''
class Exam(object):
    def __init__(self, score):
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val


class Exam2(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

if __name__ == "__main__":
    e = Exam(60)
    print e._score
    print e.get_score()

    e2 = Exam2(90)
    print e2.score
    e2.score = 100
    print e2.score