#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

ip_port = ('127.0.0.1', 40102)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

conn, addr = tcp_server.accept()

# 指定buffer_size ,得到的结果就是通过 Nagle 算法，随机接收次数。
# data1 = conn.recv(buffer_size)
# print('第1次数据', data1)
#
# data2 = conn.recv(buffer_size)
# print('第2次数据', data2)
#
# data3 = conn.recv(buffer_size)
# print('第3次数据', data3)

# 指定每次接收字节数，就不会出现粘包现象
data1 = conn.recv(5)
print('第一次数据', data1)

data2 = conn.recv(5)
print('第2次数据', data2)

data3 = conn.recv(5)
print('第3次数据', data3)
