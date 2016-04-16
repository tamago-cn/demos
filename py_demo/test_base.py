#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'

"""
@file:    test.py
@brief:   简介
@details: 详细信息
@author:  wxs
@date:    2016-04-17
"""

alist = [1, 2, 4, -5, 7]
blist = [x for x in range(1, 11, 2)]
atuple = tuple(alist)
agen = (x for x in range(1, 11, 2))
print range(10)
print type(atuple), atuple
print type(agen), agen
print list(atuple)
print enumerate(alist)
clist = []
for index, item in enumerate(alist):
    print index, item, abs(item)
    clist.append((index, item, abs(item)))

print sum(alist)
print round(float(sum(alist)) / (len(alist) + 2), 2)
print map(lambda x: x**2, alist)
print map(lambda x, y: x * y, alist, blist)
print map(None, alist, blist)
print zip(alist, blist)
print reduce(lambda x, y: x + y, atuple)
print reduce(lambda x, y: max(x, y), atuple)
print filter(lambda x: x if x > 0 else None, alist)
print alist
print alist.sort()
print clist
print sorted(clist, key=lambda x: x[1], reverse=True)

#print sorted()
#reduce
#filter
#zip