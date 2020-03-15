# docker使用的一些记录

## docker基本命令


### docker 更换源

编辑`/etc/docker/daemon.json`
```bash
{
  "registry-mirrors": [
  "https://dockerhub.azk8s.cn",
  "https://hub-mirror.c.163.com"
  ]
}
```

## dockerfile

### 创建"Dockerfile",构建属于自己的docker image

```bash
# 查看帮助
docker build --help
# 构建image 值得注意最后有一个".",从当前目录"Dockerfile"构建
docker build -t name:tag .
```

### dockerfile基本构成


以下为"Dockerfile"内容

```bash
# "#"号可以做注释
# "FROM"表示从哪个image开始构建
FROM ubuntu:18.04

# "ARG"声明一些dockerfile内部的变量参数
ARG user_name=john

# "RUN"在shell中执行一些命令,可以使用"\"换行
RUN apt update && \
	apt upgrade
# 对于参数较多的名名令可以使用下面的方式
RUN ["echo", "hello world!"]

# "CMD"用来为需要直接启动的container提供默认的命令
CMD ["executable", "param1", "param2"]

# "LABEL"以键值对的方式打标签,有多种方式,可以添加网站信息,描述等
LABEL maintainer="SvenDowideit@home.org.au"
LABEL multi.label1="value1" \
      multi.label2="value2" \
	        other="value3"


# "MAINTAINER"维护者信息
MAINTAINER "SvenDowideit@home.org.au"

# "EXPOSE"释放端口号
EXPOSE 80/tcp
EXPOSE 3000/tcp

# "ENV"声明环境变量
ENV myName="John Doe" 

# "ADD"创建新目录或文件
ADD /mydir/
ADD test /mydir/

# "COPY"复制文件
COPY test /relativeDir/

# "ENTRYPOINT" 运行最后的命令,覆盖"CMD"
ENTRYPOINT ["executable", "param1", "param2"]
# "VOLUME"
# "ARG"
# "USER"
# "WORKDIR"
```

link: https://docs.docker.com/engine/reference/builder/


### tips&tricks

```bash
# 更换安装源,更新软件更快
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g
/etc/apt/sources.list \

```

## docker compose

用来同时启动多个存在内在联系的docker container,协同运行
