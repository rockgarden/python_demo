#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
from socket import *

ip_port = ('127.0.0.1', 40002)
back_log = 5
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    cmd, addr = udp_server.recvfrom(buffer_size)
    print(cmd)

    # 执行命令，得到命令的运行结果cmd_res
    res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    err = res.stderr.read()
    if err:
        cmd_res = err
    else:
        cmd_res = res.stdout.read()

    if not cmd_res:  # 判断为空的情况
        cmd_res = '执行成功'.encode('utf-8')
    print(cmd_res)
    # 发
    udp_server.sendto(cmd_res, addr)
