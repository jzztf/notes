# linux 系统管理

## `uptime`

`uptime`显示服务器已经运行多久了

```bash
uptime
10:22:51 up  1:49,  1 user,  load average: 0.22, 0.84, 1.01
uptime -p
# 显示开机至此总时长
uptime -s
# 显示开机时间
```

## `free`

`free`查看内存使用情况的命令

```bash
free -h
              total        used        free      shared  buff/cache   available
Mem:           3.7G        2.0G        109M         47M        1.6G        2.1G
Swap:          1.9G        268K        1.9G
# -h => --human
```

## `ifconfig`

`ifconfig`查看网络

```bash
sudo apt install net-tools
ifconfig
# 查看网卡信息
```

## `htop`

`htop`是`top`的替代品

```bash
sudo apt install htop
htop
```

## `glances`

`glances`是一个跨平台的系统监控软件


**优点**
- 远程监控
- 可以在web页面监控
- 数据可以导出到elasticsearch,csv,rabbittmg,influxdb等

```bash
sudo pip install glances bottle
glances
glances -s # 开启一个galances服务器
glances -c <ip_server> # 开启客户端
glances --browser # 浏览器模式
glances -h # 寻求帮助
```

## `dstat`


`dstat`显示系统资源状态

```bash
sudo apt install dstat
dstat --top-mem --top-io --top-cpu

# 其他参数
-c  ==> cpu
-d  ==> disk
-l  ==> load avg
-u  ==> usage
-m  ==> memory
-n  ==> net
-p  ==> process
-s  ==> swap
-y  ==> system
-t  ==> time
```


