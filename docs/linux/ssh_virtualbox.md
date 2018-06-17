# ssh登陆虚拟机和分享目录

## ssh登陆虚拟主机

```bash
VBoxManage modifyvm ubuntu --natpf1 "ssh,tcp,,3022,,22"
# virtualbox -> setting -> port forwading
VBoxManage showvminfo myserver | grep 'Rule'
# check the port forwarding
sudo apt-get install openssh-server
# make sure installed openssh-server in the virtual system
ssh -p 3022 user@127.0.0.1
# user is the name in virtualbox
cd shared
watch -d -n 1 ls -l
# 使用watch监控
```

link: [how to ssh to a virtual guest externally through a host](https://stackoverflow.com/questions/5906441/how-to-ssh-to-a-virtualbox-guest-externally-through-a-host?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

## 分享目录

- 方法一

```bash
# 本机操作
sudo apt install sshfs
mkdir shared  # 同时在虚拟机创建shared_vm
sshfs user_vm@127.0.0.1:/home/user_vm/shared_vm ~/shared -p 3022
# 测试可以使用watch监测
watch -d -n 1 ls -al
```

- 方法二

```bash
# 设置virtualbox
## device -> shared folder setting -> 添加分享文件
## device -> insert guest additions CD Images -> 添加镜像
```

- 方法三

```bash
# 设置virtualbox
# device -> shared folder setting -> 添加分享文件“shared”
sudo adduser user vboxsf  # 将user加到vboxsf组中
mount shared  # 虚拟机mount
sudo mount -t vboxsf -o uid=1000,gid=1000 shared /home/user_vm/shared  # 虚拟机终端
```

- 自动挂载
    - 可以在virtualebox分享文件设置，直接设置成自动挂载
    - 也可以修改“/etc/fstab/”

```bash
# /etc/fstab
<file system>  <mount point>   <type>  <options>   <dump>  <pass>
<name_of_share>   /path/to/mountpoint   vboxsf   <options>  0   0
```

link:

- [mount remote directory ussing ssh](https://askubuntu.com/questions/412477/mount-remote-directory-using-ssh?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- [how to mount a virtualbox shared folder at startup](https://askubuntu.com/questions/252853/how-to-mount-a-virtualbox-shared-folder-at-startup)

## 端口转发

端口转发（port forwarding）是网络地址转换（network address
translation--NAT）的一个应用，它在请求信息通过路由时，重定向了地址+端口。

比如“ssh登陆虚拟机”中，将虚拟机的22端口转发到宿主机的3022端口，实现宿主机和虚拟机之间的通信。

端口转发一般常常用于虚拟机与宿主机之间通信时使用。

link: 

- [网络地址转换](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E5%9C%B0%E5%9D%80%E8%BD%AC%E6%8D%A2)
- [端口转发--port forwarding](https://en.wikipedia.org/wiki/Port_forwarding)
