# 网络管理

## ping

`ping`用来判断网络的连通性

```bash
ping -c 5 www.baidu.com  # -c 参数连接5次
```

## netstat

`netstat`现实网络状态的命令，可以查看电脑上所有的tcp，udp和套接字

```bash
man netstat
netstat -tpnl  # 查看当前用户的状态
sudo netstat - tunlp # 查看所有网络状态
```

## lsof

**linux内一切皆文件**

`lsof`命令用来查看打开的文件

```bash
man lsof
lsof
```

## traceroute

`traceroute`追踪本机到互联网另一端的主机是走的什么路径

```bash
sudo apt install traceroute
man traceroute
traceroute

```

## mtr

`mtr`也是用来路由跟踪的，另外显示丢包利率，可以更容易追踪到那个节点有问题。

```bash
sudo apt install mtr
man mtr
mtr github.com
```

## nethogs

`nethogs`查看哪些软件，哪些进程网络使用情况

```bash
sudo apt install nethogs
man nethogs
sudo nethogs
```

## iptraf

`iptraf`是一个IP网络的网络监控工具。它截取网络上的数据包，并给出了当前的IP流量在它的各条信息。

```bash
sudo apt install iptraf
man iptraf-ng
sudo iptraf-ng
```

