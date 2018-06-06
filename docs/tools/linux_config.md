# linux 系统配置

## git

[git & github](git_github.md)

- git config
- ssh-key
- github

## vim

[vim basis](vim.md) | [vim config](vim_config.md)

- vundle
- airline/airline-themes
- powerline fonts
- flake8

## zsh

[zsh](zsh.md)

- ohmyzsh
- `sudo chsh -s /bin/zsh <username>`
- `vim .zshrc`

## pip

[pip](pip.md)

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

[ipython](ipython.md)

- ipython

```bash
ipython --help
ipython profile create
# edit ~/.ipython/profile_default/ipython_config.py
```

- jupyter_notebook

