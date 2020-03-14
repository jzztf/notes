# win10下git问题汇总

1. `git status`乱码，不正常显示数字，只出现类似`\344\270\212\347\`的代码

> 同样linux下有此问题也可以使用如下命令
> `git config --global core.quotepath false`

2. 打开Git Bash，右键标题栏选择“Options”。修改Text中的Locale为“zh_CN”，Character set为“UTF-8”，关闭Git Bash。
