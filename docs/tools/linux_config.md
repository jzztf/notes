# linux 系统配置

## git

- git config

```bash
git config --global user.name "<name>"
git config --global user.email "<email>"
```

- gen ssh-key

```bash

```

- github

```bash
git clone git...
git remote add origin git...
git pull origin <master|gh-pages>
git push -u origin master
```

## vim

- vundle
- airline/airline-themes
- powerline fonts
- flake8

## zsh

- ohmyzsh

[ohmyzsh]()

- `sudo chsh -s /bin/zsh <username>`

- `vim .zshrc`

## pip

- source

```bash
# ~/.pip/pip.conf

[global]
trusted-host =  mirrors.aliyun.com
index-url = https://mirrors.aliyun.com/pypi/simple
```

- pipenv

```bash
pip install pipenv
pipenv install
pipenv --help
pipenv shell
```

- autoenv

```bash
pip install autoenv

# touch a ".env" in the project folder
# project/.env
pipenv shell
```

## ipython

- ipython

```bash
ipython --help
ipython profile create
# edit ~/.ipython/profile_default/ipython_config.py
```

- jupyter_notebook



