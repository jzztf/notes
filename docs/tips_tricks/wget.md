# wget

- 下载单个文件

`wget https://xxxx.com/xx.pdf`

- 下载以不同的文件名命名

`wget newname.pdf https://xxxx.com/xx.pdf`

- 后台下载

`wget -b https://xxxx.com/xx.pdf`

- 查看下载进度

`tail -f wget-log`

- 限速下载

`wget --limit-rate=300k https://xxxx.com/xx.pdf`


- 断点续传

`wget -c https://xxxx.com/xx.pdf`

- 伪装代理

`wget --user-agent="Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16" http://www.minjieren.com/wordpress-3.1-zh_CN.zip`

- 下载多个

```bash
cat > filelist.txt
url1
url2
url3
url4

wget -i filelist.txt
```

- 下载整个网站

`wget --mirror -p --convert-links -P ./LOCAL URL`


- 下载指定格式文件

`wget -r -A.pdf url`

可下载一个网站所有图片，视频及pdf

**参考**：[wget](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/wget.html)
