# Echo client program
import socket
import sys

HOST = '127.0.0.1'  # The remote host
PORT = 50007  # The same port as used by the server
FILE = 'output/received.txt'
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):  # socket.AF_UNSPEC, socket.SOCK_DGRAM)
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
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
# with s:
#     s.sendall(b'Wangkan')
#     data = s.recv(1024)
#     with open(FILE, 'wb') as f:
#         f.write(data)

for data in [b'Michael', b'Tracy', b'Sarah']:
    with s:
        s.sendto(data, (HOST, PORT))
        data = s.recv(1024)
        print('Received', repr(data))
    with open(FILE, 'wb') as f:
        f.write(data)

# s.shutdown(2)
# s.close()

# # 发送数据:
# s.sendto(data, (HOST, PORT))
# # 接收数据:
# data_back = s.recv(1024).decode('utf-8')
# with open(FILE, 'a') as f:
#     f.write(data_back)
