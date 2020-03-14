# python高级——James Powell


## 装饰器


```python
In :def hello():
...:    print("hello world!")
...:    
# 使用一些魔术方法，可以查看函数的基本信息
In :hello.__name__
Out:'hello'
In :hello.__module__
Out:'__main__'
In :hello.__defaults__
In :hello.__code__.co_code
Out:b't\x00d\x01\x83\x01\x01\x00d\x00S\x00'
In :hello.__code__.co_varnames
Out:()
# 模块“inspect”中的一些方法，可以追踪到代码中的函数，类的源代码
In :from inspect import getsource
In :getsource(hello)
Out:'def hello():\n    print("hello world!")\n'
In :from inspect import getfile
In :getfile(hello)
Out:'<ipython-input-19-e3ad41635293>'
In :from inspect import getmodule
In :getmodule(hello)
Out:<module '__main__'>
```

### 简单装饰器

> 装饰器的主要作用在于计时，记录日志等

- 简单的计时，我们可以将计时代码写入计时函数

```python

```
