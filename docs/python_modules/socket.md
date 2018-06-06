# socket-套接字模块


```python
# socket对象

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## socket.socket()接受的两个参数

socket.AF_INET      ==>     ipv4

socket.SOCK_STREAM  ==>     TCP编程
socket.SOCK_DGRAM   ==>     UDP编程

# 绑定套接字（server）
socket.bind((HOST,PORT))

## HOST & PORT

HOST = '127.0.0.1'  ==> 或者其他服务器名
PORT = 8001         ==> 数字格式

# 监听绑定的地址
s.listen(5)         ==> UDP不需要监听

# 
s.accept()          ==> 返回一个元组(conn,address)，一个新的套接字对象和地址
conn, addr = s.accept()
## conn是一个新的socket-object用于发送和接受数据；
## addr是绑定在该套接字另一端的链接地址
## 关闭连接
conn.close()

# 关闭套接字对象
s.close()

# 接受数据
s.recv(bufsize[,size])      ==> TCP
s.recvfrom(bufsize[,size])  ==> UDP

# 发送数据
socket.send(bytes[,flags])  ==> TCP
socket.sendto(bytes, addr)  ==> UDP

```
