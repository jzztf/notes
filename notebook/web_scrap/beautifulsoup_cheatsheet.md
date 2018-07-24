# 总的来说最常用的是soup对象`findall`方法

```python
import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language')
soup = BeautifulSoup(r.text, 'lxml')

links = soup.find_all("a")
for link in links:
    print(link['href'])

# 使用正则
external_links = soup.find_all('a', href=re.compile(r"http(s)?://,*"))
for link in external_links:
    print(link['href']) # link ==> tag对象

internal_links = soup.find_all('a', href=re.compile(r"^/wiki/,*"))
for link in internal_links:
    print(link['href'])
```


# 四种对象类型

- Tag
- Navigablestring
- Beautifulsoup
- Comments

比较常用就是“BeautifulSoup”对象：`soup_object = BeautifulSoup(html)`；“Tag”对象是对“BeautifulSoup”对象筛选的结果：`tag_object = soup_object.find_all("tag_name")`或者`tag_object = soup_object("a")`

# 导航文档树

- 自上而下

```python
soup.head
soup.title
soup.body.b
soup.find_all("a")
# .contents会以列表形式返回"body"标签内所有内容
soup.body.contents
# .children返回一个可迭代对象
soup.body.children
# .descendants返回所有后代，".contents"和".children"返回子代
soup.body.descendants
# 如果对象是NavigableString, ".string"可返回字符串
soup.title.string
# .stripped_strings返回不带空格的字符串
soup.title.stripped_strings
```

- 自下而上

```python
soup.body.parent
soup.body.parents
```

- 前后

```python
soup.body.p.next_sibling
soup.body.p.previous_sibling
soup.body.p.next_siblings
soup.body.p.previous_siblings
```

- 前前后后

```python
soup.body.p.next_element
soup.body.p.previous_element
soup.body.p.next_elements
soup.body.p.previous_elements
```

## 遍历文档树

- 过滤器类型
    - 字符串过滤器
        - `soup.find_all('b')`
    - 正则表达式过滤器
        - `soup.find_all(re.compile("^b"))`
        - `soup.find_all('a', string=re.compile("story"))`
    - 列表过滤器
        - `soup.find_all(['a', 'b'])` 
    - True真值过滤器
        - `soup.find_all(True)`
    - 函数过滤器
        - `soup.find_all(has_class_but_no_id)`

```python
def has_class_but_no_id(tag):
   return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)

def not_lacie(href):
    return href and not re.compile("lacie").search(href)

soup.find_all(href=not_lacie)


```
- find_all()方法
    - 语法`soup.find_all(name,attrs,recursive,string,limit,**kwargs)`
    - `name`参数
        - tag名称“a”
    - 关键字参数
        - 通过css类进行选择
        - **注意**：`class_`
        - `soup.find_all(class_="sister")`
    - 字符串参数
        - `soup.find_all(string="story")`
    - limit参数
        - `soup.find_all('a', limit=2)` 
    - recursive参数
        - `soup.find_all('a', recurisve=False)` 
    - 像调用`find_all()`一样调用标签`tag`
        - `soup("a")` 

**以下方法都是更细化对soup对象或tag对象遍历**

- find()方法
- find_parents()和find_parent()
- find_next_siblings()和find_next_sibling()
- find_previous_siblings()和find_previous_sibling()
- find_all_next()和find_next()
- find_all_previous()和find_previous()
- CSS选择器

```python
soup.select("title")
soup.select("body a")
soup.select("head > title")
soup.select(".sister")
soup.select("#link1")
soup.select('a[href="http://example.com/elsie"]')
soup.select('a[href^="http://example.com"]')
soup.select_one(".sister") # 寻找第一个

```

## 修改文档树

- 改变标签名称和属性
    - 修改`.string`属性
    - `append()`
    - `NavigableString()`和`.new_tag()`
    - `insert()`
    - `insert_before()`和`insert_after()`
    - `clear()`
    - `extract()`
    - `decompose()`
    - `replace_with()`
    - `wrap()`
    - `unwarp()`

## 输出

- 漂亮打印
    - `soup.prettify()`
    - `non-pretty`
- 输出格式
    - ... 
- `get_text()`
   - `get_text()`可以获取整个文档，或者某标签下的文本信息

## 解析器

不同的解析器有不同的优缺：
- `html.parser`beautifulsoup默认解析器，支持自动补全
- `xml`速度快，但不会自动补全


## 编码

BeautifulSoup能够自动将ASCII转成utf-8

如果传入的文本属于特殊编码可以传入关键字参数`from_encoding="iso-8859-8"`类似的

```python
# 自主选择编码模式
soup = BeautifulSoup(markup, from_encoding="ISO-8859-8")
# 如果确切知道其不属于某种编码格式，可以使用exclude_encodings
soup = BeautifulSoup(markup, exclude_encodings=["ISO-8859-8"])
```

## 复制beautifulsoup对象

**深拷贝**和**浅拷贝**，python中的声明语句不会拷贝对象，只是引用。

- **深拷贝**：拷贝对象及其子对象
- **浅拷贝**：浅拷贝产生的的对象本身是新的，但是它的内容不是最新的，只是对原子对象的引用

link: <https://docs.python.org/3.6/library/copy.html>

```python
import copy
p_copy = copy.copy(soup.p)
```

