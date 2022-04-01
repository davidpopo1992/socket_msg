# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:17:40 2022

@author: davidpopo
"""

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #初始化实例
s.bind(("localhost",9000)) #绑定本机的ip与端口
s.listen(2)  #开始监听
print("等待客户端连接")


count=0
while count<=2: #当一个连接断开后，可以进入下一个连接
    client_conn,client_addr=s.accept()   #等待客户端链接
    count+=1
    print(f"第{count}次连接,对应客户端: {client_addr}")

    while True:
        data=client_conn.recv(1024)  #从客户端接收消息，最大为1024节
        if not data:  #代表客户端断开了
          print(f"客户端{client_addr}断开了")
          break   #如果客户端断开了，则进入母循环，等待另一个客户端连接
        print(f'服务器接收消息: {data.decode()}')
        client_conn.send(data.decode().upper().encode()) #将数据变成大写再还给客户端

s.close()   #关闭服务器