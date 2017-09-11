#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午4:27
# @Author  : philoxmyu
# @Contact : philoxmyu@gmail.com


def multiply(x, y):
    return x * y


if __name__ == "__main__":
    from functools import partial
    double = partial(multiply, 2)
    print double, type(double)
    print double(3)