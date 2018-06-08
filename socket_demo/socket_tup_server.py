#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: nulige

# 实现ntp时间服务器
import time
from socket import *

ip_port = ('127.0.0.1', 50011)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # 数据报套接字
udp_server.bind(ip_port)

while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print(data)

    if not data:
        fmt = '%Y-%m-%d %X'  # 如果用户没有输入内容，就返回默认格式的时间
    else:
        fmt = data.decode('utf-8')
    back_time = time.strftime(fmt)

    udp_server.sendto(back_time.encode('utf-8'), addr)
