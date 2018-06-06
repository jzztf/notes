# pip & pipenv & autoenv

## source

```bash
# ~/.pip/pip.conf

[global]
trusted-host =  mirrors.aliyun.com
index-url = https://mirrors.aliyun.com/pypi/simple
```

## pipenv

```bash
pip install pipenv
pipenv install
pipenv --help
pipenv shell
```

## autoenv

```bash
pip install autoenv

# touch a ".env" in the project folder
# project/.env
pipenv shell
```
