# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:05:48 2022

@author: davidpopo
"""

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #初始化实例
s.bind(("localhost",9000)) #绑定本机的ip与端口
s.listen(2)  #开始监听
print("等待客户端连接")
client_conn,client_addr=s.accept()   #等待客户端链接
client_conn.send("相与客户端建立连接".encode())   #向客户端发送消息
data=client_conn.recv(1024)  #从客户端接收消息，最大为1024节
print('服务器接收到的消息: ',data.decode())
client_conn.close() #关闭与客户端的连接
s.close()   #关闭服务器