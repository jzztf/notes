# datetime and time

```python
import datetime, time

datetime.datetime.now()
# datetime.datetime.now()返回一个当前的日期和时间
# datetime.datetime()函数可以被传入年月日时分秒的整数,生成新的datetime对象,并传入(year,month,day,hour,moinute,second)
dt = datetime.datetime(2018,1,2,10,30,50)
dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second
# (2018, 1, 2, 10, 30, 50)
datetime.datetime.fromtimestamp(1519983366.9375882)
# datetime.datetime.fromtimestamp()unix纪元时间戳到给定参数之后的时间戳
t = datetime.datetime.now()
for x in range(1000):
    x
t2 = datetime.datetime.now()
t2 > t
# datetime对象支持操作符比较
```

## `.strftime()`

strftime指令

|strftime指令|含义|
|:-:|:-:|
|%Y|四位数:'2018'|
|%y|两位数18:'18','00-99'|
|%m|数字: '3','01-12'|
|%B|英文全: 'March'|
|%b|英文简: 'Mar'|
|%d|全月天: '4','01-31'|
|%j|全年天: '65','001-366'|
|%w|全周天: '3','0-6'|
|%A|英文全: 'Monday'|
|%a|英文简: 'Mon'|
|%H|24小时: '18','01-23'|
|%I|12小时: '6','01-12'|
|%M|分: '00-59'|
|%S|秒: '00-59'|
|%P|早晚:'AM/PM'|
|%%|%号|
    
使用:

只针对datetime对象, 其实其是使用格式化字符串方法实现的

```python
import datetime,time

dt = datetime.datetime.now()
dd = time.time()

dt.strftime('%Y/%m/%d')
# ==>'2018/03/03'
dd.strftime('%Y/%m/%d')
# AttributeError: 'float' object has no attribute 'strftime'

```

`datetime.datetime.strptime()`


`.strftime()`的反向操作

```python
datetime.datetime.strptime('2018/03/17','%Y/%m/%d')
# ==> datetime.datetime(2018, 3, 17, 0, 0)
```

## python时间函数


关于时间的三种对象:

- unix时间戳,time模块中的time属性,自1970/1/1/零时起秒数: `time.time()`
- datetime对象,datetime模块中的属性,包含一系列整型数值,保存在(year,month,day,minute,seconds等属性中)
  - `datetime.datetime,now()`获得对象"datetime.datetime(2018, 3, 3, 16, 33, 23, 308114)"
- timedelta对象,datetime模块中的属性, 表示一段时间
  - `datetime.timedelta(days=10,hours=10,minutes=8,seconds=9)`获得对象"datetime.timedelta(10, 36489)"

关于时间的函数,及其参数和返回值

- `time.time()`获取当前unix时间戳
- `time.sleep(seconds)`程序睡眠几秒
- `datetime.datetime(year,month,day,hour,minute,second)`将整型数转化为datetime对象
- `datetime.datetime.now()`获取当前时间的datetime对象
- `datetime.datetime.fromstamp(time.time())` == `datetime.datetime.now()`获取某个unix时间戳的datetime对象
- `datetime.timedelta(weeks,days,hours,minutes,seconds,milliseconds,microseconds)`某个时间段时间
- `total_seconds()`用于timedlta对象,返回timedlta对象的秒数
- `strftime(format)`方法返回一个format格式的字符串
- `datetime.datetime.strptime(timestr,format)`返回一个date对象

