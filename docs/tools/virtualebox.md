# virtualbox的相关使用

## 以“headless”无前端模式开启

```bash
VBoxManage list vms  # 查看当前所有虚拟机
VBoxHeadless-startvm [ubuntu]
```

## 设置ssh远程登陆

```bash
VBoxManage modifyvm myserver --natpf1 "ssh,tcp,,3022,,22"
VBoxManage showvminfo myserver | grep 'Rule'
sudo apt-get install openssh-server
ssh -p 3022 user@127.0.0.1
```

link: [How to SSH to a VirtualBox guest externally through a host?](https://stackoverflow.com/questions/5906441/how-to-ssh-to-a-virtualbox-guest-externally-through-a-host?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

## linux虚拟机如何使用宿主机的shadowsocks代理上网

```bash
$ ip route show
# 基本上都是10.0.2.2
$ export http_proxy=http://10.0.2.2:1080
$ export https_proxy=https://10.0.2.2:1080
# 或者直接在firefox里设置
```
