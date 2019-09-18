# HOW TO INSTALL EMACS IN LUBUNTU

1. PREREQUISITES

```bash
$ sudo apt update && apt upgrade -y
$ sudo apt install build-essential libncurses-dev
```

2. DOWNLOAD THE SOURCE CODE

```bash
$ wget https://mirrors.tuna.tsinghua.edu.cn/gnu/emacs/emacs-26.1.tar.gz
$ tar -xzvf emacs-26.1.tar.gz
```

3. BUID THE SOURCE CODE

```bash
$ cd emacs-26.1/
$ ./configure --without-x --with-gnutls=no
$ make
$ sudo make install
$ emacs
```

4. START EMACS SERVER

```bash
$ git clone https://github.com/jzztf/dotemacs.d.git .emacs.d
$ emacs # build&install packages
$ emacs --daemon
$ echo "alias e='emacsclient -t'" >> .bashrc
$ e
```


