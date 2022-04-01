# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:16:00 2022

@author: davidpopo
"""

import socket
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #初始化实例
cli.connect(("localhost",9000))
data=cli.recv(1024)
print("从服务器端接收到的消息为: ",data.decode())
cli.send("客户端也给服务器端发送一条消息".encode())
cli.close()