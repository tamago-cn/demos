#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'

"""
@file: construct_demo.py
@brief: 简介
@details: 详细信息
@author: wxs
@date: 2016-05-14
"""
from construct import *

class TcpObject(object):
    def __init__(self):
        pass

Login = Struct(
    'Login',
    Bytes('Username', 20),
    Bytes('Password', 20)
)
LoginAck = Struct(
    'LoginAck',
    UBInt32('Level')
)

TCP_PROTOCAL = Struct(
    'TCP_PROTOCAL',
    UBInt32('Length'),
    Enum(
        UBInt32('PK_Type'),
        LOGIN=101,
        LOGINACK=102
    ),
    Switch(
        'Info',
        lambda ctx: ctx.PK_Type,
        {
            'LOGIN': Login,
            'LOGINACK': LoginAck
        }
    )
)

user_name = '%-20s' % ('user', )
password = '%-20s' % ('password', )
print user_name, password

login_obj = TcpObject()
setattr(login_obj, 'Username', user_name)
setattr(login_obj, 'Password', password)
a = Login.build(login_obj)
print a, login_obj

login_ack_obj = TcpObject()
setattr(login_ack_obj, 'Level', 2)
b = LoginAck.build(login_ack_obj)

tcp_protocal_obj = TcpObject()
tcp_protocal_obj.Length = 4
tcp_protocal_obj.PK_Type = 101
tcp_protocal_obj.Info = login_obj

# c = TCP_PROTOCAL.build(tcp_protocal_obj)
test_str = '\x65\x00\x00\x00\x00\x00\x00\x65user                password            '
print len(test_str)
d = TCP_PROTOCAL.parse(test_str)
print d

test_str = '\x00\x00\x00\x65\x00\x00\x00\x66\x00\x00\x00\x02'
print len(test_str)
d = TCP_PROTOCAL.parse(test_str)
print d


a = Container(
    Username=user_name,
    Password=password
)

b = Container(
    Level=2
)

c = TCP_PROTOCAL.build(
    Container(
        Length=3,
        PK_Type='LOGIN',
        Info=a
    )
)

def pack(PK_Type, Info, check=False):
    if check:
        crc16 = None
        return
    else:
        return TCP_PROTOCAL.build(
            Container(
                Length=3,
                PK_Type=PK_Type,
                Info=Info
            )
        )
print 'a:', a
print 'b:', b
print 'c:', c.encode('hex')

print '0000000300000065757365722020202020202020202020202020202070617373776f7264202020202020202020202020'.decode('hex')