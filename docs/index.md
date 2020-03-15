# 使用mkdocs存储零散笔记

## 基本命令

```bash
$ mkdocs --help

MkDocs - Project documentation with Markdown.

Options:
  -V, --version  Show the version and exit.
  -q, --quiet    Silence warnings
  -v, --verbose  Enable verbose output
  -h, --help     Show this message and exit.

Commands:
  build      Build the MkDocs documentation
  gh-deploy  Deploy your documentation to GitHub Pages
  new        Create a new MkDocs project
  serve      Run the builtin development server
```

## 编辑发布

```bash
# 生成,编辑mkdown文件到/docs目录

# 将原文档提交到github
git push

# 将文档生成html
mkdocs build

# 本地查看
mkdocs serve

# 发布到github个人页面
mkdocs gh-deploy
```
