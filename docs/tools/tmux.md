# tmux

link：<https://gist.github.com/ryerh/14b7c24dfd623ef8edc7>

## 多窗口

> 类似于在视图界面操作多窗口一样，只是窗口最小化在tabbar。

|commands|actions|
|-------|-------|
|`prefix c`|创建新窗口，tabbar带`*`号的就是当前所在|
|`prefix 0`|进入窗口0|
|`prefix 1`|进入窗口1|
|`prefix s`|预览所有窗口|
|`prefix x`|关闭当前窗口|
|`prefix d`|退出tmux|

## 分屏

> 将一个窗口分成若干屏，同时显示


### 先对`～/.tmux.conf`进行设置

```
#command-key
set -g prefix C-x

# split window
unbind '"'
# vertical split (prefix -)
bind - splitw -v
unbind %
# horizontal split (prefix |)
bind | splitw -h


#up
bind-key k select-pane -U
#down
bind-key j select-pane -D
#left
bind-key h select-pane -L
#right
bind-key l select-pane -R
```

### commands

|commands|actions|
|-------|--------|
|`prefix &#124;`|添加垂直窗口|
|`prefix -`|添加水平窗口|
|`prefix arrow-key`|改变窗口大小|
|`prefix o`+`prefix arrow-key`|窗口之间切换|
|`prefix n`|后一个窗口|
|`prefix p`|前一个窗口|
|`prefix f`|查找窗口|
|`prefix ,`|重命名当前窗口|
|`prefix &`|关闭当前窗口|
|`prefix x`|关闭tmux|

### 改变窗口大小

```
prefix to enter command mode

PREFIX : resize-pane -D          当前窗格向下扩大 1 格
PREFIX : resize-pane -U          当前窗格向上扩大 1 格
PREFIX : resize-pane -L          当前窗格向左扩大 1 格
PREFIX : resize-pane -R          当前窗格向右扩大 1 格
PREFIX : resize-pane -D 20       当前窗格向下扩大 20 格
PREFIX : resize-pane -t 2 -L 20  编号为 2 的窗格向左扩大 20 格
```
