# 字典


字典就是键值对的集合，什么是键，什么是值，取决于希望怎么索引。字典是python中唯一的映射类型。键可以是数字，字符串，也可以是元组。**元组**在实际应用中也是很广泛的存在，


```python
# 创建字典
d = {}

# update方法更新字典，如果有相应键值对则更新，没有则添加
d.update(a=1,b=2,c=3)

# 调用值
d['b']
d.get('b')

# 使用get的优点就是，在没有访问到值时不会报错，也可以在没有访问到值，添加默认参数
d['d']
d.get('d')
d.get('d',0)

# 可使用“in”关键字判断
'a' in d

# 获取键值元组
d.keys()
d.values()

# 对于层级嵌套的映射需求
# 比如，a，b两个大类下面又分若干小类有如下几种解决方式

# 方法1,使用特殊结构关联
d['{}_{}'.format('a','c')] = 'T'
d['a_c']

# 方法2,使用嵌套字典关联
d['a'] = {'c':'T','d':'U'}
d['a']['c']

# 方法3,使用元组
d[('a','c')] = 'T'
d[('a','c')]
```

python3的字典对键值对有记忆功能，python2可使用collections中的OrderedDict()记忆。