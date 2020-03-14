# USE SCP WITH ALIAS

- [USE SCP WITH ALIAS](https://superuser.com/questions/291778/unable-to-use-scp-with-a-bash-alias)

## first step:

alias hostNameAlias='ssh hostName@xx.xx.xxx.xx'

## second step:

vim ~/.ssh/config

```
Host hostNameAlias
HostName xx.xx.xxx.xx
User hostName
Port 22
```

## third step:

```bash

# connect
ssh hostNameAlias
# scp from local to remote
scp /some/file hostNameAlias:/path/to/storage/loaction
# scp from remote to local
scp hostNameAlias:/some/file /local/path/
```

## parameters

- `-r` 递归复制整个目录
- `-P` 数据传输端口号
