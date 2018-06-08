#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

BUFSIZE = 1024
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

qq_name_dic = {
    '努力哥': ('127.0.0.1', 40102),
    '刘哥': ('127.0.0.1', 40102),
    '李哥': ('127.0.0.1', 40102),
    '王哥': ('127.0.0.1', 40102),
}

while True:
    qq_name = input('请选择聊天对象: ').strip()  # 选择字典中的聊天对象，再发送消息
    while True:
        msg = input('请输入消息,回车发送: ').strip()
        if msg == 'quit': break
        if not msg or not qq_name or qq_name not in qq_name_dic: continue
        udp_client_socket.sendto(msg.encode('utf-8'), qq_name_dic[qq_name])

        back_msg, addr = udp_client_socket.recvfrom(BUFSIZE)
        print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' % (addr[0], addr[1], back_msg.decode('utf-8')))

udp_client_socket.close()
