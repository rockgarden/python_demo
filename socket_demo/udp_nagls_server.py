from socket import *

ip_port = ('127.0.0.1', 40102)
back_log = 5
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # 数据报
udp_server.bind(ip_port)

data1 = udp_server.recvfrom(10)
print('第1次', data1)

data2 = udp_server.recvfrom(10)
print('第2次', data2)

data3 = udp_server.recvfrom(10)
print('第3次', data3)

data4 = udp_server.recvfrom(2)
print('第4次', data4)
