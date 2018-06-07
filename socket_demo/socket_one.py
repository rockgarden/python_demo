# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # 绑定端口:
# s.bind(('127.0.0.1', 50007))
# print('Bind UDP on 9999...')
#
# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     reply = 'Hello, %s!' % data.decode('utf-8')
#     s.sendto(reply.encode('utf-8'), addr)

import socket

FILE = 'output/received.txt'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 50007))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
    with open(FILE, 'a') as f:
        f.write(data)

s.shutdown(2)
s.close()
