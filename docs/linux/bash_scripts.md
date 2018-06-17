# bash结构化命令

## 变量

- 首字母（a-z, A-Z）
- 中间不能有空格，可以使用下划线
- 不能使用标点符号
- 不能使用bash关键字

```bash
$ name="python"  # bash变量赋值，中间不加空格
$ echo $name  # 调用变量添加“$”符号
python
$ echo ${name}  # 也可以添加“{}”包裹变量名
python
$ echo 'name: $name'  # 单双引号之间的区别，单引号会原文呈现，不会转换变量
name: $name
$ echo "name: $name"  # 双引号会自动转换变量
name: python
$ echo "name: {$name}"  # 错误使用“{}”
name: {python}
$ echo "name: ${name}"  # “{}”的使用是为了确认变量边界
name: python
$ echo "name $names"  # 因找不到“$name”变量，只显示name
name
```

## 字符串

linux默认所有字符为字符串

```bash
$ var=1
$ var=$var+1  # 默认字符都为字符串
$ echo $var
1+1
$ (( var+=1  ))  # “(( commands ))”双括号表示运算，括号内与命令之间要保持空格
$ echo $var
3
$ (( var++  ))
$ echo $var
4
```

## 特殊环境变量

- `$0` 当前脚本名称
- `$num` num从1开始，表示传入的第几个参数
- `$#` 传入脚本的参数个数
- `$*` 所有参数，组成的一个字符串
- `$@` 所有参数，数组，每个参数都是独立的字符串
- `$?` 当前shell进程，上一个命令的返回值，如果上一个命令成功执行，则`$?`为0
- `$$` 当前shell进程pid
- `$!` 后台运行的最后一个进程的pid
- `$-` 现实shell使用的当前选项
- `$_` 之前命令的最后一个参数

```bash
# x.sh
---
#!/bin/bash

echo $1 $2 $3
---

$ chmod +x x.sh
$ ./x.sh a b c  # 运行脚本-1
a b c
$ bash x.sh a b c  # 运行脚本-2
$ sh x.sh a b c  # 运行脚本-3
```

## 数组

```bash
$ array=(a b c)  # 创建数组
$ echo ${array[*]}  # 查看数组元素
a b c
$ array[3]=d  # 添加元素
$ echo ${array[*]}
a b c d
$ unset array[3]  # 删除某元素
$ echo ${array[*]}
a b c
```

## 反引号

输出命令结果

```bash
$ echo `date`
2018年 06月 17日 星期日 14:29:35 CST
$ echo `echo my date is `date``  # 反引号内不可使用反引号，若使用需要转义
my date isdate
$ echo `echo my date is \`date\``
my date is 2018年 06月 17日 星期日 14:30:21 CST
```

## 命令执行顺序

```bash
$ echo "date"; date  # 分号，似的命令依次进行
date: 
2018年 06月 17日 星期日 14:48:18 CST

$ echo apple > xx.txt
$ echo banana >> xx.txt
$ cat xx.txt | grep apple  # 管道符号，将前者的命令输出传递给后面的命令
apple

$ `exit 0` && echo 1  # 前一个命令执行成功时，执行后面的命令
1
$ `exit 1` && echo 1  
$ `exit 0` || echo 1
$ `exit 1` || echo 1  # 前一个命令执行失败时，执行后面的命令
1
```

## 控制语句---if

```bash
# 语法
if [condition]
then
    command
elif [condition2]
    command2
else
    commandN
fi

# 实例
$ if [[ -f xx.txt ]]; then echo "xx.txt exists"; fi
xx.txt exists
# -f 判断文件存在，返回真
# -d 判断文件为目录，返回真
# -x 判断文件存在，并且可执行返回真

```

## 控制语句---case

比elif更有效的判断选择

```bash
# 语法
case expression in
    pattern )
        statements ;;
    pattern )
        statements ;;
    ...
esac

# 实例
xx.sh
---
#!/bin/bash

case a in
	$1 )
		echo "first parameter is a";;
	$2 )
		echo "second parameter is a";;
    * )
        echo "Error"
esac
---
$ ./xx.sh
$ ./xx.sh b a
second parameter is a
$ ./xx.sh a b
first parameter is a
$ ./xx.sh
Error
$ ./xx.sh c d
Error
```

## 控制语句---for

```bash
# 语法
for var in argument-list
do
    command
done

# 实例
$ for var in a b c d
> do
> echo $var
> done
a
b
c
d
```

## 控制语句---while

```bash
# 语法
while condition
do
    command-list
done
# 实例
$ n=1
$ while [ $n -lt 5 ]; 
> do 
> echo "$n is less than 5"
> (( n++ ))
> done
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
```

## 控制语句---until

与whhile类似，但是不同：
- while condition，满足condition条件下，下面命令执行
- until condition，执行下面命令，知道condition条件达成

```bash
$ n=1
$ until [ $n -ge 5 ]
> do
> echo "$n is less than 5"
> (( n++ ))
> done
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
```

## 控制语句---break

break就是执行之后代码，不再循环

```bash
$ while [ $n -lt 5 ]
> do
> if [ $n -eq 3 ]
> then
> break
> fi
> echo $n  # 满足break条件之后，之后代码不再执行，故只有1,2
> (( n++ ))
> done
1
2

```

## 控制语句---continue

continue就是不执行之后的代码，跳到下一轮循环

```bash
$ n=1
$ while [ $n -lt 5 ]
> do
> (( n++ ))
> if [ $n -lt 3 ]
> then
> continue  # 满足continue条件之后错过之后代码，继续循环
> fi
> echo $n
> done
3
4
5

```

## 函数

```bash
# 语法
[ function ] funcname [ () ]  # 方括号内为可选内容

{
    action;
    [ return int; ]
}
# 实例

$ hello () { echo 'hello world'; }
$ hello
hello world
$ hello () { echo "hello $1"; }
$ hello world
hello world
```

link: <http://tldp.org/LDP/Bash-Beginners-Guide/html/index.html>
