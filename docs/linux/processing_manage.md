# linux 进程管理

## ps（process status）

进程状态

```bash
man ps  # 展示所有帮助
ps -ef  # 显示所有进程，所有格式

# 常用的几个命令
ps -fu john|less  # 找用户名为john启动的进程
ps U $USER  # 使用环境变量，效果同上
ps aux --sort pmem|less  # 根据内存占用排序
ps aux --sort pcpu|less  # 根据CPU占用排序
ps -f --ppid=2962  # 列出父pid是2962的进程
```

## grep

查询

```bash
man grep  # 展示帮助
grep -i  # ignore忽略大小写
grep -v  # invert反转，过滤
```

## top

动态显示系统状态

```bash
man top
# 主要按键
P   ==> 根据CPU使用百分比进行排序 
M   ==> 根据内存进行排序
i   ==> 使top不显示任何闲置或者僵死命令
```

## 终止进程

```bash
man kill

kill -9 -1  # 杀掉所有能杀掉的进程
kill -9 1024  # 杀掉pid为1024的进程
kill -TERM pid  # -15等同于-TERM，生产环境下
```

### linux signal信号

- 信号9是终止进程
- 信号15是终止terminal

link: <https://linux.die.net/Bash-Beginners-Guide/sect_12_01.html>

## pgrep/pkill

```bash
man grep
pgrep xpad | xargs kill -9  # 搜索xpad并杀掉
pkill xpad   # 搜索xpad并杀掉
```

## fg/bg

```bash
sleep 600 &  # 睡眠600s
[1] 9717
fg  # 将后台程序放到前台
[1]  + 9717 running    sleep 600
^Z  # “ctrl + z” 冻结
[1]  + 9717 suspended  sleep 600
bg  # 转至后台
[1]  + 9717 continued  sleep 600
sleep 600 &
[1] 10034
sleep 500 &
[2] 10043
sleep 400 &
[3] 10053
jobs  # 显示后台程序
[1]    running    sleep 600
[2]  - running    sleep 500
[3]  + running    sleep 400
fg %3  # 将3号后台程序放到前台
[3]  - 10053 running    sleep 400
```

## watch

重复检测程序变化

```bash
man watch
watch -d  # 高亮显示不同
watch -n 1  # 1s 检测一次，默认为2s检测一次
watch -d ls -l  # 检测当前文件夹内文件情况“ls -l”
```

## crontab（定时任务）

定时任务用于备份文件十分有用

```bash
crontab  # 会引导选择使用哪种编辑器
man crontab  # 展示帮助
crontab -e  # 编辑自动任务文件，关闭后，任务自动启动
crontab -l  # 查看当前自动任务
# 任务格式就是“时间”+“命令”
# 时间表示“分（0-59）”+“时（0-23）”+“天（1-31）”+“月（1-12）”+“周（0-7）”
# 中间以空格隔开，0和7都表示周末
# *号表示所有时间
# 分隔符“/”可以表示每个多长时间
# 每周一早上5点执行下面备份任务
0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 每5分钟执行一次
*/5 * * * * tar -zcf /var/backups/home.tgz /home/

# 系统默认的定时任务位于/etc/crontab

```

link: <https://linux.cn/article-7513-1.html>

