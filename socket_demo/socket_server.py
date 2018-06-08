# Echo server program
# Support both IPv4 and IPv6
# 客户端发送空格，服务端也会接收
import socket
import sys

print('Python %s on %s' % (sys.version, sys.platform))

HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces '127.0.0.1'
PORT = 50007  # Arbitrary non-privileged port
MaxClients = 5
buffer_size = 1024

s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    socketFamily, sockType, proto, canonName, sa = res
    try:
        s = socket.socket(socketFamily, sockType, proto)
    except OSError as msg:
        s = None
        continue
    try:
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 就是它，在bind前加
        s.bind(sa)  # 绑定端口-服务端网卡IP地址和端口
        s.listen(MaxClients)  # backlog连接池（也叫半链接）
    except OSError as msg:
        print("OSError: " + str(msg))
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(MaxClients)

# while True:
conn, addr = s.accept()  # 服务器阻塞
print('双向链接是', conn)
print('客户端地址', addr)
while True:
    with conn:
        # 接收数据
        data = conn.recv(buffer_size)  # 收缓存为空，则阻塞
        if not data: break
        # conn.send(data.upper())
        reply = 'Hello, %s!' % data.decode('utf-8')
        print(reply)
        conn.send(reply.encode('utf-8'))
conn.close()
s.close()

# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     reply = 'Hello, %s!' % data.decode('utf-8')
#     s.sendto(reply.encode('utf-8'), addr)
