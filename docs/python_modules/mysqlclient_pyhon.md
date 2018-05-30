# mysqlclient-python

## install

[repo](https://github.com/PyMySQL/mysqlclient-python)


```bash
$ pip install myqlclient-python
# prerequisits
$ sudo apt-get install python3-dev
```

## user guide

- connect

```python
import MySQLdb

db = MySQL.connect(
    host="localhost",
    user="username",
    passwd="password",
    db="student")
```
- create table

```python
cursor = db.cursor()

cursor.execute("CREATE TABLE profile(id INT PRIMARY KEY,name VARCHAR(30),age INT)")
```
- insert data

```python
cursor.execute("INSERT INTO profile(id,name,age) values(1,'mei',12)")
```

- select data

```python
cursor.execute("SELECT * FROM profile")
all = cursor.fetchall()
for _ in all:
    print(_)


```

- delete data

```python

```

- update data

```python

```
