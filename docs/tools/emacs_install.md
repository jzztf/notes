# EMACS INSTALL

```bash
sudo apt update
sudo apt install emacs
# ubuntu install emacs24
git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d
# too slow
wget https://github.com/syl20bnr/spacemacs/archive/master.zip
unzip -o master.zip -d ~/.emacs.d
emacs
# start emacs 
# configuration
vim .spacemacs

(defun dotspacemacs/user-init ()
  (setq configuration-layer--elpa-archives
      '(("melpa-cn" . "http://elpa.emacs-china.org/melpa/")
        ("org-cn"   . "http://elpa.emacs-china.org/org/")
        ("gnu-cn"   . "http://elpa.emacs-china.org/gnu/")))
  "Initialization function for user code.
It is called immediately after `dotspacemacs/init', before layer configuration
executes.
 This function is mostly useful for variables that need to be set
before packages are loaded. If you are unsure, you should try in setting them in
`dotspacemacs/user-config' first."
  )

emacs
# restart emacs install packages
alias e="emacsclient -t"
```
