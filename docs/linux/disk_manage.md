# linux 磁盘管理

## du

查看某个目录所占空间大小

```bash
du /tmp  # 查看tmp目录大小
du /tmp -h  # 以易读的方式呈现大小（KB/MB/GB/TB）
du /tmp -s  # 只显示该目录的大小，不显示内嵌目录
```

## df

查看已挂在磁盘的总容量，使用容量，剩余容量

```bash
df  # 查看挂在的磁盘
df -h  # 以易读的方式呈现大小
```

## fdisk

查看磁盘使用情况

```bash
sudo fdisk -l  # 列出当前磁盘使用情况
sudo fdisk /dev/sdb1  # 管理sdb1磁盘
m  # 帮助信息
d  # 删除分区
n  # 创建分区
w  # 写入，确认都没问题时才写入！
q  # 退出
```

## fstab（自动挂载）

如果要设置自动挂载，可设置此文件

```bash
cat /etc/fstab
# 5个字段
# <file system>  <mount point>  <type>  <options>  <dump>  <pass>
```

### 参数

- `<file systems>` 要挂载的分区或存储设备.
- `<dir>` 的挂载位置。
- `<type>` 要挂载设备或是分区的文件系统类型，常见的类型：ext4, ntfs, swap 及 auto。 设置成auto类型，mount 命令会猜测使用的文件系统类型，对移动设备非常有用。
- `<options>` 挂载时使用的参数，注意有些 参数是特定文件系统才有的。一些比较常用的参数有：
  - `auto` 在启动时或键入了 mount -a 命令时自动挂载。
  - `noauto` 只在你的命令下被挂载。
  - `defaults` 使用文件系统的默认挂载参数
- `<dump>`  工具通过它决定何时作备份. dump 会检查其内容，并用数字来决定是否对这个文件系统进行备份。 允许的数字是 0 和 1 。0 表示忽略， 1 则进行备份。大部分的用户是没有安装 dump 的 ，对他们而言 <dump> 应设为 0。
- `<pass>` `fsck` 读取 <pass> 的数值来决定需要检查的文件系统的检查顺序。允许的数字是0, 1, 和2。 根目录应当获得最高的优先权 1, 其它所有需要被检查的设备设置为 2. 0 表示设备不会被 fsck 所检查。

### 文件系统标识

`/etc/fstab`可以以三种不同的方法表示文件系统：内核名称，UUID，或label。UUID和label与磁盘顺序无关，不会在重新插拔存储设备随机更改顺序。

```bash
lsblk -f  # 查看当前挂载磁盘UUID或label
```

link: <https://wiki.archlinux.org/index.php/Fstab_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)>

