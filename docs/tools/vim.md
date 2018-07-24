# vim 操作


## 可用于生产环境的配置

### 需求

- 新建文件，关闭文件
    - `:e file`新建缓冲区打开file文件案
    - `:bn`后一个缓冲区
    - `:bp`前一个缓冲区
    - `:bd`关闭缓冲区
    - `:ls`列出所有打开的缓冲区
- 使用tab标签
    - `:tabnew` | `:tabnew file`打开新标签
    - `^w + T`将窗口变成标签（分屏的窗口）
    - `gt` | `:tabnext` | `:tabn`切换到下一个标签
    - `gT` | `:tabprev` | `:tabp`切换到上一个标签
    - `#gt`切换到第`#`个标签
    - `:tabmove #`移动标签到第`#`位
    - `:tabclose` | `:tabc`关闭当前标签
    - `:tabonly` | `:tabo`关闭其他标签
    - `:tabdo command`在所有标签中执行命令
    - `:tabdo q`关闭所有标签
- 分屏
    - `:sp file`水平分割窗口
    - `:vsp file`垂直分割窗口
    - `^w + s`水平分割窗口
    - `^w + w`窗口见切换
    - `^w + q`退出窗口
    - `^w + v`垂直分割窗口
    - `^x + h-j-k-l`切换窗口
- 找到最近修改的文件
- 找到函数定义
- 找到声明
- 替换
- 回滚
- google search
- ipython交互

## 小技巧

使用系统剪切板

```bash
# 安装必要包
$ sudo apt-get install vim-gui-common
# 使用，选中目标后
“+y
```

实际上只是在原命令`y`前添加`”+`

links：
- <https://www.zhihu.com/question/19863631>
- <https://github.com/ruanyf/articles/blob/master/dev/vim/operation.md>
