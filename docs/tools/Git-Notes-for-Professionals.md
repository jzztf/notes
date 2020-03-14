#+TITLE: org-mode
#+TOC: headlines

# 开始使用git

## 1.1
## 1.2
## 1.3 分享代码

远程服务器:

`git init --bare /path/to/repo.git`

> 为有效节省服务器端空间,可以使用"--bare" 参数, 该参数只生成 ".git" 内部的文件

本地仓库

`git remote add origin ssh://username@server:/path/to/repo.git`

将本地仓库推送到远程服务器

`git push --set-upstream origin master`

> "--set-upstream" 就是参数 "-u", 之后可以直接使用 "git pull"

## 1.4 设置用户名与电子邮件

在进行提交代码时,需要认证身份

全局设置

```bash
git config --global user.name "username"
git config --global user.email "useremail"
```

单个项目设定

```bash
cd /path/to/my/repo
git config user.name "username"
git config user.email " useremail"
```

移除全局身份设定

```bash
git config --global --remove-section user.name
git config --global --remove-section user.email
# 也可以重新设定全局身份为空；或者直接修改"~/.gitconfig"
# check
git config --global user.useConfgOnly true
```

## 1.5 设定远程upstream

与githubfork的原项目保持更新

```bash
# 查看远程分支
git remote -v
# 设置upstream
git remote add upstream https://github.com/projectname/repo.git
# 拉取
git fetch https://github.com/projectname/repo.git
# 合并到自己fork的项目上
git merge upstream/master
# 推送到自己的fork库
git push 
```


