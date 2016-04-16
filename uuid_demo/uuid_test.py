#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'

"""
@file:    uuid_test.py
@brief:   简介
@details: 详细信息
@author:  wxs
@date:    2016-04-17
"""
import os
import sys
import uuid

reload(sys)
sys.setdefaultencoding('utf-8')
name = 'wxs'
namespace = 'testspace'
print type(name)
print 'timebased uuid uuid1:', uuid.uuid1()
print 'md5sum uuid uuid3:', uuid.uuid3(namespace, name)
print 'sha1sum uuid uuid5:', uuid.uuid5(namespace, name)