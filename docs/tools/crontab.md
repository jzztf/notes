# CRONTAB-定时任务


## SET DEFAULT EDITOR

```bash
~/.profile
EDITOR vim; export EDITOR
```

## CRON FILE

- 第一列分钟0-59
- 第2列小时0～23（0表示子夜）
- 第3列日1～31
- 第4列月1～12
- 第5列星期0～7（0和7表示星期天）
- 第6列要运行的命令

## CREATE CRON FILE

```bash
vim <user>cron

# (put your own initials here)echo the date to the console every
# 15minutes between 6pm and 6am
0,15,30,45 18-06 * * * /bin/echo 'date' > /dev/console

crontab <user>cron
crontab johncron
# 执行前面的命令
```

## OTHER COMMANDS

```bash
crontab -l
# list all crontab
crontab -e
# edit crontab
crontab -r
# 删除
```


