# vim 设置

## install vim

- install
```bash
sudo apt install vim
```

- install  vundle(vim plugin manager)

  - repo: [VundleVim/Vundle.vim](https://github.com/VundleVim/Vundle.vim)


### install vim plugin

- air-line/air-line-theme

  - repo: [vim-airline/vim-airline](https://github.com/vim-airline/vim-airline)
  - themes: [screenshots](https://github.com/vim-airline/vim-airline/wiki/Screenshots)

  - plugin(add to .vimrc):
```
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
let g:airline_theme='simple'
```

- markdown-preview

  - repo: [iamcco/markdown-preview.vim](https://github.com/iamcco/markdown-preview.vim)

  - plugin:
```
Plugin 'iamcco/markdown-preview.vim'
" 设置自动打开
"let g:mkdp_auto_start = 1
" 设置F8快捷键操作
nmap <silent> <F8> <Plug>MarkdownPreview        " for normal mode
imap <silent> <F8> <Plug>MarkdownPreview        " for insert mode
nmap <silent> <F9> <Plug>StopMarkdownPreview    " for normal mode
imap <silent> <F9> <Plug>StopMarkdownPreview    " for insert mode
```

### other setting

```
" set coding
set encoding=utf-8

set nu

au BufNewFile,BufRead *.js, *.html, *.css, *.md
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2

" Split Layouts,<:sv filename>;<:vs filename>
set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
```
