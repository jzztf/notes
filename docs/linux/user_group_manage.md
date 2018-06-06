# linux 用户和用户组管理

## 访问控制（可读，可写，可执行）

### 文件权限

```bash
ll .vim
drwxr-xr-x 17 ztf ztf 4.0K 5月  31 05:57 bundle
ll .vimrc
-rw-rw-r-- 2 ztf ztf 2.1K 5月  31 06:00 .vimrc
```

### 文件属性描述

- `d` 表示该文件为“dir”目录
- `-` 表示该文件为普通文件
- `l` 表示该文件是一个链接“link”
- `rwx` 表示该文件的读写执行权限
  - 表示文件的字符后面有3组“rwx”分别表示：文件属主，用户组，其他用户。
  - 用英文就是`u`-`g`-`o`表示user，group和others
  - `a`表示all

### 修改文件权限

**方法一**

```bash
touch test.sh
ll test.sh
-rw-rw-r-- 1 ztf ztf 0 6月   6 11:39 test.sh
chmod a+x test.sh  # 赋予所有用户和组执行权限，”+“号表添加 
ll test.sh       
-rwxrwxr-x 1 ztf ztf 0 6月   6 11:39 test.sh
chmod g-w test.sh  # 去掉组的写入权限，”-“号表减去
ll test.sh       
-rwxr-xr-x 1 ztf ztf 0 6月   6 11:39 test.sh
chmod o=--- test.sh  # 去掉其他人的所有权限，”=“号表赋值
ll test.sh         
-rwxr-x--- 1 ztf ztf 0 6月   6 11:39 test.sh
```

**方法二：八进制表示法**

- `1`只有执行权限
- `2`只有写入权限
- `4`只有读取权限

> 类似上`=`号表示

```bash
touch test.sh
ll test.sh
-rw-rw-r-- 1 ztf ztf 0 6月   6 11:51 test.sh
chmod 775 test.sh  # 按照创建文件时的权限，为所有用户添加执行权限
ll test.sh
-rwxrwxr-x 1 ztf ztf 0 6月   6 11:51 test.sh
chmod 755 test.sh  # 允许用户以外的组和其他有读和执行的权限，没有写的权限
ll test.sh       
-rwxr-xr-x 1 ztf ztf 0 6月   6 11:51 test.sh
```

## 创建删除用户

```bash
sudo useradd john

# 参数
-m          ==> 创建home目录
-g group    ==> 将该用户归属于group组
-s /bin/zsh ==> 指定bash
-p password ==> 指定密码，默认不指定

sudo passwd john  # 换行后，指定密码
su - john  # 以john用户名登入

sudo userdel -r john  # 删除john用户，并删除其home信息
```

> 用户信息都会添加到”/etc/passwd“，可使用”tail“命令查看

## 创建删除组

```bash
sudo groupadd group_1  # 添加组group_1
sudo gpasswd -a john group_1  # 将john添加到用户组group_1
sudo gpasswd -d john group_1  # 将john从group_1删除
sudo groupdel group_1   # 删除组group_1
```

## sudo权限

sudo可以使得不用root而执行一些权限

```bash
sudo cat /etc/sudoers  # 可以查看”/etc/sudoers“

# 设置sudo免密
root    ALL=(ALL:ALL) ALL
john    ALL=(ALL:ALL) ALL NOPASSWD: ALL  
# 如果无效将下面的group行也添加nopasswd: all

```

>  免密操作要慎用!

link: <https://www.jianshu.com/p/5d02428f313d>


