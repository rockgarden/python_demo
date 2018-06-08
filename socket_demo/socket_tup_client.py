#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: nulige

from socket import *

ip_port = ('127.0.0.1', 50011)  # 服务端IP+端口
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)  # 数据报套接字

while True:
    msg = input('>>:').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)

    data, addr = udp_client.recvfrom(buffer_size)
    print('ntp服务器的标准时间是', data.decode('utf-8'))
