# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:33:20 2022

@author: davidpopo
"""

import socket
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #初始化实例
cli.connect(("localhost",9000))

while True:
    msg=input("input your msg>>>").strip()
    if msg=="q":
        break
    cli.send(msg.encode())   
    data=cli.recv(1024)
    print(f"从服务器端接收到的消息为: {data.decode()}")

cli.close()