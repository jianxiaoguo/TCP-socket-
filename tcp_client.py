# -*-coding:utf-8-*-

from socket import *
# 创建套接字
client_soc = socket(AF_INET, SOCK_STREAM)

cli_addr = ("127.0.0.1", 8888)
client_soc.connect(cli_addr)
# print(a)
msg = input("李输入:")
while True:
    if msg == "q":
        break
    # 发送
    client_soc.send(msg.encode())
    # 接受,回显
    data_CB = client_soc.recv(1024)
    # print("cb")
    print("小王:"+data_CB.decode())
    msg = input("李输入:")

client_soc.close()


