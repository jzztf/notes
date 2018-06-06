# hexo安装设置

## node.js/npm

- 国内源: <https://npm.taobao.org/>

- 设置:

``` bash
# config设置
npm config set registry https://registry.npm.taobao.org
# 命令行指定
npm install package-name --registry https://registry.npm.taobao.org
# ~/.npmrc文件中加入下行
registry = https://registry.npm.taobao.org
```
