# -*-coding:utf-8-*-
from socket import *
# 创建套接字
s_sock = socket(AF_INET, SOCK_STREAM)

# 端口复用
s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定端口.IP
ser_addr = ("", 8889)
s_sock.bind(ser_addr)
# 监听  128表示最多可以监听128个客户端的请求,超过128时其他链接等待
s_sock.listen(128)
# accp获取建立的链接, 多个客户端时accept阻塞等待,没调用一次获取一次连接
client_sock, client = s_sock.accept()
while True:
    # recv阻塞等待数据请求
    data = client_sock.recv(1024)
    msg = data.decode().strip()
    print("李:"+msg)
    # 处理请求
    a = (msg == "q")
    # print(a)
    if a or not data:
        print("quit")
        break
    # 回显
    data = input("小王输入:")
    client_sock.send(data.encode())

# 关闭真正通信的套接字
client_sock.close()

# 关闭服务器的套接字
s_sock.close()


# 结果返回
