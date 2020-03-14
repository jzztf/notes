# python 模块 random

## 生成随机数


```python
# generating random numbers
import random
random.random()
# ==> 0.38223875002738705
# 返回n, 0 <= n < 1.0 随机数
```

## 种子随机数


```python
# seed
random.seed(10)
for _ in range(3):
    print(random.random())
```

- `random.seed([x])`会根据参数值,计算随机数,当调用`random.random()`时还能取到原来的值
- `random.seed`方法的作用是给随机数对象一个种子值，用于产生随机序列。对于同一个种子值的输入，之后产生的随机数序列也一样。
- 通常是把时间秒数等变化值作为种子值，达到每次运行产生的随机系列都不一样。

## 保存状态


```python
# saving state

```

## 随机整数


```python
# random integers
random.randint(1,101)
# ==> 84
random.randrange(1,101,5)
# 1-101, 以步长为5, 取随机整数
# random.randrange(start,stop,step)

```

## 随机选择


```python
# picking random items
l = [x for x in range(1,10)]
random.choice(l)
# 从一个序列随机选取一个数
```

## 序列


```python
# Permutations


```
