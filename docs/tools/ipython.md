# ipython 使用技巧

## 定制profile

```bash
# default ipython create ~/.ipython/profile_default/
$ ipython profile create
# create custom ipython profile
$ ipython profile create simple
# ipython create ~/.ipython/profile_simple/
# set custom profile in profile_simple/ipython_config.py
# set custom startup file in profile_simaple/startup/
# use custom profile
$ ipython --profile='simple'
# show all profile 
$ ipython profile list
# locate the profile
$ ipython locate profile simple
```

## ipython_config


```python
## lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = ['autoreload 2']

## A list of dotted module names of IPython extensions to load.
c.InteractiveShellApp.extensions = ['autoreload']

```

autoreload 2: Reload all modules (except those excluded by %aimport) every time before executing the Python code typed.[link](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html?highlight=autoreload%202)

## custom prompts

```python
# coding: utf-8

#----------------------------------------------------
# .ipython/profile_default/startup/00-prompts-start.py
#----------------------------------------------------
# 参考: <https://ipython.readthedocs.io/en/stable/config/details.html#custom-prompts>
# 将此文件添加到".ipython/profile_default/startup/"即可

from IPython.terminal.prompts import Prompts, Token

class MyPrompt(Prompts):
    def in_prompt_tokens(self,cli=None):
        return [(Token.Prompt,'In :')]
    def out_prompt_tokens(self,cli=None):
        return [(Token.Prompt,'Out:')]
    
ip = get_ipython()
ip.prompts = MyPrompt(ip)
```

该文件随python启动，重定义了提示符号，便于复制粘贴进行演示代码。
