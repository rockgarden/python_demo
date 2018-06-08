# Echo client program
import socket
import sys

HOST = '127.0.0.1'  # The remote host
PORT = 50007  # The same port as used by the server
FILE = 'output/received.txt'
back_log = 5
buffer_size = 1024

# tcp_client = socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_client.connect(HOST, PORT)

s = None
# (host, port, family=0, type=0, proto=0, flags=0)
for res in socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM):  # socket.AF_UNSPEC, socket.SOCK_DGRAM)
    af, st, proto, canonName, sa = res
    try:
        s = socket.socket(af, st, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)

# while True:
#     msg = input('>>:')  # 发送空格到自己的发送缓存中
#     # msg=input('>>:').strip()  # 去掉空格
#     s.send(msg.encode('utf-8'))
#     print('客户端已经发送消息')
#     data = s.recv(buffer_size)  # 收缓存为空则阻塞
#     print('收到服务端发来的消息是', data.decode('utf-8'))

# with s:
#     s.sendall(b'Wangkan')
#     data = s.recv(1024)
#     data = s.recv(1024)
#     with open(FILE, 'wb') as f:
#         f.write(data)

for data in [b'Michael', b'Tracy', b'Sarah']:
    with s:
        s.sendto(data, (HOST, PORT))
        print('客户端已经发送消息')
        data = s.recv(buffer_size)  # 收缓存为空则阻塞
        print('Received', repr(data))
    with open(FILE, 'wb') as f:
        f.write(data)

# s.shutdown(2)
s.close()

# # 发送数据:
# s.sendto(data, (HOST, PORT))
# # 接收数据:
# data_back = s.recv(1024).decode('utf-8')
# with open(FILE, 'a') as f:
#     f.write(data_back)
