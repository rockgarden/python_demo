#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

ip_port = ('127.0.0.1', 50002)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # 数据报套接字
udp_server.bind(ip_port)
print('服务端开始运行了')
while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print(data)

    udp_server.sendto(data.upper(), addr)  # upper() 小写变大写
