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
# scp
scp /some/file tencent:/path/to/storage/loaction
```
