# spacemacs 使用和配置


## 简单记录下折腾

- 熟悉`evil`模式 
- 安装`mode line`(失败) 

`telephone-line`

- 折腾主题

```bash
SPC SPC package-install
SPC SPC load-theme
SPC SPC enable-theme
SPC T h ==>
(set-default dospacemacs-themes '(list-themes-here))
```

## layer和package

- package: emacs lisp文件的集合，其可能在ELPA或MELPA仓库，github 或者在本地
- layer: 内置在spacemacs内的设置组件，一个layer可包涵一个或多个package

## 常用快捷键

|按键|说明|
|----|----|
|`SPC f`|打开file操作菜单|
|`SPC p`|打开project操作菜单|
|`SPC b`|打开buffer操作菜单|
|`SPC w`|打开window操作菜单|
|`SPC q`|打开quit操作菜单|
|`SPC h`|打开help操作菜单|
|`SPC T`|打开theme操作菜单|


## cheatsheet

**vim操作！**

```bash
# 文件
-----------------------------
open file       ==> SPC f f
save file       ==> SPC f s
create file     ==> SPC f f
find file       ==> SPC p f
edit .spacmacs  ==> SPC f e d

# 查找文本
-----------------------------
/               ==> 本文中搜索词
*               ==> 查找光标所在词的下一个
#               ==> 查找光标所在词的上一个
:nohl           ==> 取消高亮搜索词
SPC /           ==> 项目中搜索词

# 导航 
-----------------------------
^               ==> 行首
$               ==> 行尾
w               ==> 右1词首
5w              ==> 右5个词词首
e               ==> 右1词尾
b               ==> 左1词首
j/k/h/l         ==> 上下左右
22j             ==> 下22行
22k             ==> 上22行
{               ==> 下1段
}               ==> 上1段
[[              ==> 上1函数
]]              ==> 下1函数
^ d             ==> 下1页
^ u             ==> 上1页
gg              ==> 文首
G               ==> 文尾
g;              ==> 上次修改位置

# 窗口布局
------------------------------
SPC w           ==> 窗口布局菜单
SPC w -         ==> 下分1屏
SPC w /         ==> 右分1屏
SPC w 2         ==> 分2列
SPC w j/k/h/l   ==> 移动焦点

# 编辑
------------------------------
v               ==> 可视模式
y               ==> 复制
yw              ==> 复制词
yy              ==> 复制行
3yy             ==> 复制3行
y$              ==> 复制至行尾
d               ==> 删除
x               ==> 删除字符
dw              ==> 删除词
dd              ==> 删除行
3dd             ==> 删除3行
d$              ==> 删除至行尾
df)             ==> 删除至括号内
u               ==> 撤销
>               ==> 右移1字符
2>              ==> 右移2字符
<               ==> 左移1字符
2<              ==> 左移2字符
```

## emacs 操作

```
## 缓冲区buffer

SPC-b h ==> back to home
SPC-b N ==> new buffer 
SPC-b n ==> next buffer
SPC-b p ==> previous buffer
SPC-b d ==> kill this buffer
SPC-b m ==> kill other buffer
SPC-b P ==> paste clipboard to this buffer
SPC-b Y ==> yank this buffer to clipboard

---

## 文件

SPC-f f ==> find-file
SPC-f s ==> save-file
SPC-f r ==> helm-recent-file
SPC-f T ==> neotree-show
SPC-F t ==> neotree-toggle
SPC-F R ==> rename-the-file 

---

## 窗口

SPC-w - ==> split-window-below
SPC-w / ==> split-window-right
SPC-w + ==> window-layout-toggle
SPC-w 2 ==> layout-double-columns
SPC-w 3 ==> layout-three-columns
SPC-w = ==> balance-windows
SPC-w _ ==> maximize-horizontally
SPC-w d ==> delete-window

### evil mode
SPC-w H/h ==> 
SPC-w J/j ==> 
SPC-w K/k ==> 
SPC-w L/l ==>
SPC-w S/s ==> aplit-window-below
SPC-w V/v ==> split-window-right
SPC-w up/down ==> move-cursor-up/down
SPC-w up/down ==> move-cursor-right/right
SPC-w S-up/down ==> move-cursor-very-up/down
SPC-w S-right/left ==>move-cursor-very-right/left

## org-mode

open an org file

SPC-m p ==> org-pomodoro
SPC-m T ==> show-TODO-tree

### promodoro

SPC-m p ==> star-pomodoro

### presentation

SPC SPC org-present

h ==> previous slide
l ==> next slide
q ==> quit

### org-mime

SPC m M ==> in message-mode buffers convert into html email
SPC m m ==> send current buffer as HTML 

### org-projectile

SPC a o p ==> capture a TODO for the current project
SPC u SPC a o p ==> capture a TODO for any given project
SPC p o ==> go to the TODOs for the current project

```

## others

- `SPC s c` 清除搜索高亮

