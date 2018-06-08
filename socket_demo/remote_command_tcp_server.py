#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
from socket import *

ip_port = ('127.0.0.1', 40001)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    conn, addr = tcp_server.accept()
    print('新的客户端链接', addr)
    while True:
        # 收
        try:
            cmd = conn.recv(buffer_size)
            if not cmd: break  # MAC笔记本处理方法
            print('收到客户端的命令', cmd)

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
            # 发
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break

conn.close()
