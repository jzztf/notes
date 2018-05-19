# 如何编写强密码

## 藏头诗

使用诗词名做提示，使用其头字母；也可以使用自己的口头禅等常见字符串的拼音首字母。

|tip|code|
|:---:|:------|
|`静夜思-李白`|`cyjdlb`|
|`富强民主文明和谐`|`fqmzwmhx`|

## 字母-数字切换

数字和小写字母有些是不宜分辨的，出于保密的需要可以设定密钥时进行一下切换，即使自己在哪里记录的明文密码暴露，依然可以有一定的私密性。

|number|alphabet|
|:------:|:--------:|
|`1`|`l`|
|`2`|`z`|
|`6`|`b`|
|`8`|`x`|
|`9`|`q`|
|`0`|`o`|

|weak|strong|
|:----:|:------|
|`wang1996`|`wanglqqb`|
|`liu520`|`1iu5zo`|

## 数字和符号

将原密码中的数字在键盘上通过`shift`切换成符号，或者切换奇数或偶数。**缺点**：依赖键盘

|weak|strong|
|:----:|:------|
|`wang1996`|`wang!((^`|
|`liu520`|`liu5@)`|

## 键盘平移

将原密码中的字母在键盘上进行平移，可以都平移一个，也可以奇数偶数错开，奇移1，偶移2.**缺点**: 依赖键盘

|weak|strong|
|:----:|:------|
|`wang1996`|`esmh1996`|
|`wang1996`|`edmj1996`|

## 数学等式

将原密码中的数字利用等式等符号连接起来，添加一些特殊字符

|weak|strong|
|:----:|:------|
|`wang1996`|`wang19+96=115`|
|`wang1996`|`wang19-96=-77`|

## hash

使用特定文件的hash值，只要文件不发生变化，hash值是不会变化的。

```bash
# for windows
certutil -hashfile filename MD5
certutil -hashfile filename SHA1
certutil -hashfile filename SHA256

# for linux
md5sum hello.txt 
d41d8cd98f00b204e9800998ecf8427e  hello.txt
# upload the file to your email or other place in the internet
```

可以在特定的文件留一些线索将密码所属联系起来。**缺点**：需要设备和服务

## git commit ID

git commit ID也是取自部分hash值

```bash
mkdir code
cd code
git init .
echo hello > hello.txt
git add .
git commit -m "hello code"
git log --pretty=oneline
061de870c59eccc496af0b75c88b6627a4f1b837 (HEAD -> master) hello code
# push it to your secret repo
# leave some tips in the new file or the commit message
```

可以使用自己原有仓库的commit
ID，也可以创建一个私密仓库，存储自己的commit信息。**缺点**：需要设备和服务

## 记在最后

- 一般认为`字母`+`数字`+`符号`达到一定长度，短时间内暴力破解几乎不可能。鉴于平时网路密钥，既要容易记，又要提升难度的要求，**最好的密码**就是在不改变原密码记忆习惯的前提下，适当使用以上部分手法进行加强。
- 对于一些不长使用，但又要很强的安全级别的密钥，可以主体使用hash和commit ID，适当组合其他手法进行设定。
- **再强的密码也不要共用**，针对不同网站设定特定字符转换机制,比如在原密码第二位加上特定网站的第一个拼音字母：

|website|weak|strong|
|-------|----|------|
|`baidu`|`wang1996`|`wbdang1996`|
|`zhihu`|`wang1996`|`wzhang1996`|
|`github`|`wang1996`|`wgang1996`|


参考：[随想](https://program-think.blogspot.com/2010/06/howto-prevent-hacker-attack-3.html)
