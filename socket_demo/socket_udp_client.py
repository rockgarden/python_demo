from socket import *

ip_port = ('127.0.0.1', 50002)  # 服务端IP+端口
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)  # udp数据报套接字

while True:
    msg = input('>>:').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)
    # 数据，ip地址+端口
    data, addr = udp_client.recvfrom(buffer_size)
    print(data.decode('utf-8'))
