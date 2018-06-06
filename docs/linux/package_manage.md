# linux 包管理

## dpkg

dpkg是linux底层的包管理软件，不会解决依赖之间的问题

```bash
dpkg -l  # 列出所有包
dpkg -l | grep firefox  # 列出所有安装包，查找firefox
dpkg -L firefox  # 列出某一包安装的文件
dpkg -S ~/.npmrc  # 查找某一文件所属程序
sudo dpkg -i package.deb  # 安装.deb安装包
sudo dpkg -r package.deb  # 卸载包
```

## apt/apt-get

Advanced Packaging Tool (APT) 

> 比apt-get有更好的交互体验

```bash
sudo apt install package  # 安装包
sudo apt remove package  # 移除包，但会留一些个人配置或信息的文件
sudo apt purge package  # 比之remove删的更多点
sudo apt autoremove  # 自动移除当前所有包不需要的依赖（可能是安装其他包，安装的依赖，当之前的包被移除后，这些依赖也就没用了）
sudo apt search package  # 查找包
sudo apt show package  # 显示给定包的信息以及其依赖的信息
sudo apt list  # 显示所有包
sudo apt list --installed  # 显示已安装
sudo apt edit-source  # 编辑"/etc/apt/sources.list"文件
sudo apt update  # 更新源
sudo apt upgrade  # 更新可更新包
```

### sources.list

**如果只是用`apt`安装，可以只留`deb`开头的**

- `deb`行关联二进制预编译软件包，可以通过`apt`安装
- `deb-src`行关联用于编译二进制软件包的源代码，通过`apt-get source $package`，随后进行编译

**根据需求选择软件库**

- `main` canoical支持的免费和开源
- `universe` 社区支持的免费和开源
- `restricted` 官方支持的非完全自由软件
- `multiverse` 非官方支持的非自由软件

**更新软件源**

```bash
deb http://cn.archive.ubuntu.com/ubuntu/ bionic main restricted
deb http://cn.archive.ubuntu.com/ubuntu/ bionic universe
deb http://cn.archive.ubuntu.com/ubuntu/ bionic multiverse

deb http://cn.archive.ubuntu.com/ubuntu/ binoic-updates main restricted
deb http://cn.archive.ubuntu.com/ubuntu/ binoic-updates universe
deb http://cn.archive.ubuntu.com/ubuntu/ binoic-updates multiverse

deb http://cn.archive.ubuntu.com/ubuntu/ binoic-security main restricted
deb http://cn.archive.ubuntu.com/ubuntu/ binoic-security universe
deb http://cn.archive.ubuntu.com/ubuntu/ binoic-security multiverse

# 使用vim编辑可使用s替换命令，更换特定源
# “:,$s/cn.archive.ubuntu.com/mirrors.aliyun.com/g”
```
## aptitude & synaptic

- aptitude 终端的菜单式带界面的包管理
- synaptic 可视化包管理器

```bash
sudo aptitude install package  # 命令行下使用aptitude
sudo aptitude remove package
```

