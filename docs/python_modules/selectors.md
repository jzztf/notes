selectors工作原理

就像我们要编辑很多文件，当文件被送过来时，先要注册下，加入一个书签，等待处理，当我们手头的工作处理完了，将其接过来处理，解除书签。

I/O复用？？

？？？
link：<https://www.rddoc.com/doc/Python/3.6.0/zh/library/selectors/?highlight=selectors#module-selectors>

```python
import socket
import selectors

HOST = '127.0.0.1'
PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)
sock.bind((HOST, PORT))
sock.listen(5)

sel = selectors.DefaultSelector()
# selectors.DefaultSelector会自动选择符合当前系统的最有效的方法

print(f'Server start at: {HOST}:{PORT}')


def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print(f'received "{data}" from {conn.getpeername()}')
        conn.send(bytes(f'Server received {data}', 'utf-8'))
    else:
        sel.unregister(conn)  # 解除注册
        conn.close()


def accept(sock, mask):
    """接入连接"""
    conn, addr = sock.accept()
    print(f'Connected by {addr}')
    conn.setblocking(0)
    sel.register(conn, selectors.EVENT_READ, read)
    # 为selector注册一个文件对象，监测它的I/O事件
    # 参数：一个socket链接，EVENT_READ可写入事件


sel.register(sock, selectors.EVENT_READ, accept)
# 监测socket对象是否可读写，以执行accept
# accept接受的参数是否为之前的两个参数？

"""
register(fileobj,events,data=none)

data 是一个不透明对象（data is an opaque object.），也可通过部分，也可以阻塞部分
"""


while 1:
    events = sel.select(0.5)
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
```
