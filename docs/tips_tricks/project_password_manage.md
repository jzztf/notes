# 妥善管理密钥

links：[Miguel Grinberg - Oops! I Committed My Password To GitHub! - PyCon 2018](https://www.youtube.com/watch?v=2uaTPmNvH0I)

mega-tutorial 中就是推荐使用环境变量来管理项目的密钥等信息。如今可以使用[autoenv](https://github.com/kennethreitz/autoenv)，创建`.env`文件，同时将其排除在版本控制外，写入`.gitignore`，这样就不会将密钥传至github了。


```bash
#1 ignore .env in .gitignore
.env

#2 put these statments into /project/.env

export PASSWORD='mypassword'
export SECRET_KEY='mypassword'
export database_url='mysql://user:password@server/db'

#3 use the env values in the project
# os.environ对象为字典类型，可使用d[k]和get()方法获取相应值

password = os.environ['PASSWORD']
secret_key = os.environ.get('SECRET_KEY')
database_url = os.environ.get('DATABASE_URL','sqlite:///')
# 默认获取‘DATABASE_URL‘，若未指定则用后面的字符串作为默认值
```
