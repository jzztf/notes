# git 和 github 基础教程

## zsh中git插件的几个基础命令

```bash
gst ==> git status
gcam ==> git commit -a -m
gp ==> git push
gl ==> git pull
gaa ==> git add --all
gcmmsg ==>  git commit -m
```

``` bash
# 安装git
sudo apt install git

# 为git添加个人信息,本地提交使用的个人信息
git config user.name 'user_name'
git config useer.email 'user_email'

# 为github添加ssh
## 生成ssh-key
ssh-keygen -t rsa -b 4096 -C "user_email"
# 添加ssh-key到ssh-agent
## 启动ssh-agent到后台
eval "$(ssh-agent -s)"
## 将ssh添加到ssh-agent
ssh-add ~/.ssh/id_rsa

# 复制ssh-pub
## 安装xclip
sudo apt-get install xclip
## 复制到剪切版
xclip -sel clip < ~/.ssh/id_rsa.pub

# 本地添加远程仓库
git remote add origin https://github.com/xxx/xxx.github.io.git
git push -u origin master
git pull
git push

# 更换https->ssh, 就无需输入用户名和密码了
git remote set-url origin git@github.com:xxx/xxx.github.io.git

# 查看当前远程分支
git remote -v

# 本地克隆远程仓库
git clone https://github.com/xxx/xxx.github.io.git

# 创建分支
...

```

