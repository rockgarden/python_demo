# Echo server program
# Support both IPv4 and IPv6
import socket
import sys

HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces '127.0.0.1'
PORT = 50007  # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        # 绑定端口
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()

with conn:
    print('Connected by', addr)
    while True:
        # 接收数据
        data = conn.recv(1024)
        if not data: break
        reply = 'Hello, %s!' % data.decode('utf-8')
        conn.send(reply.encode('utf-8'))

# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     reply = 'Hello, %s!' % data.decode('utf-8')
#     s.sendto(reply.encode('utf-8'), addr)
