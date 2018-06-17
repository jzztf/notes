# 迭代器，生成器，协程

迭代器，生成器，协程的关系：
- 实现`__iter__`和`__next__`方法的对象就是**迭代器**
- **生成器**有`__next__`方法，本质上也是**迭代器**，使用`yield`替换了`return`，一次生成一个结果。
- **协程**中`yield`作为参数，阻塞程序继续，等待传入数据，才能继续

## 迭代器（iterator）

### 可迭代（iterable）

> python中任意的对象，只要它定义了可以返回一个迭代器的`__iter__`方法，或者支持下表索引的`__getitem__`方法，那么它就是一个可迭代对象。

**可迭代对象**并不表示其就是一个迭代器

```python
In :l = [1, 2, 3]
In :l.__iter__  # 列表”l“拥有方法”__iter__“，但不具有”__next__“方法
Out:<method-wrapper '__iter__' of list object at 0x7fcfee025b88>
In :l.__next__
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-14-39daa3570050> in <module>()
----> 1 l.__next__

AttributeError: 'list' object has no attribute '__next__'
In :next(l)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-cdc8a39da60d> in <module>()
----> 1 next(l)

TypeError: 'list' object is not an iterator
In :ll = iter(l)  # 使用“iter()”函数将列表生成“列表迭代器”
In :next(ll)
Out:1
In :next(ll)
Out:2
In :next(ll)
Out:3
In :next(ll)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-20-f4a50bb27fab> in <module>()
----> 1 next(ll)

StopIteration:  # 迭代结束，触发“StopIteration”异常
```

### 迭代器实例

实现`__iter__`和`__next__`的对象就是迭代器，其中`__iter__`方法返回迭代器本身，`next`方法返回容器下一项内容，没有后续元素时，抛出`StopIteration`异常

```python
class Fib:
    def __init__(self, max):
        self.a = 0
        self.b = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
       fib = self.a
       if fib > self.max:
            raise StopIteration
       self.a, self,b = self.b, self.a + self.b
       return fib
```

## 生成器（generator）

生成器本质上是一个迭代器，只是表达更简洁

### 生成器表达式

## 协程（coroutine）

yield作为参数被传入

当调用`send`方法时，就是协程

## 回调函数


