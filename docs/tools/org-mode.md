ORG MODE
===

links:
- [org-mode](https://orgmode.org/)
- [orgguide](https://orgmode.org/orgguide.pdf)

> Org is amode for keeping notes, maintaing TODO lists, and doing project planning with a fast effective plain-text system.


[features](https://orgmode.org/features.html)
===

* [editing](https://orgmode.org/manual/Document-structure.html#Document-structure)
> navigate through headlines and (un)fold (sub)sections of Org documents easily. 
* [planning](https://orgmode.org/manual/TODO-items.html#TODO-items) | [dates/times](https://orgmode.org/manual/Dates-and-times.html#Dates-and-times)
> used as a TODO lists manager and as a planner. 
* [clocking](https://orgmode.org/manual/Clocking-work-time.html#Clocking-work-time)
> clock in and out and to produce nice reports easily.
* [agenda](https://orgmode.org/manual/Agenda-views.html#Agenda-views) | [commands](https://orgmode.org/worg/org-tutorials/org-custom-agenda-commands.html)
> it is easy to focus on what you need to do for each context. 
* [capturing](https://orgmode.org/manual/Capture.html#Capture)
> Adding TODO items to your .org files is called capturing. 
* [tables](https://orgmode.org/manual/Built_002din-table-editor.html#Built_002din-table-editor)
>  a great plain-text table editor.
* exporting
> Org is an authoring and publication tool. 
* source code
> Org makes literate programming a handy and natural way to deal with code. 
* with moble(iphone) 

document structure
---

* outlines
* headings
* visibility cycling
* motion
* structure editing
* sparse trees
* plain lists
* drawers
* blockks
* footnotes
* orgstruct mode
* org syntax

---

DOCUMENT STRUCTURE
---

- Outlines

org模式下可以通过`TAB`键或者`S TAB`键，展开合并文档结构。

- Headings

```
* top-level-heading
** level-2
*** level-3
    some text
*** level-3
    more text
```

- Visibility cycling

```
# TAB
## Subtree cycling

,-> FOLDER -> CHILDREN -> SUBTREE --.
'-----------------------------------'

# S TAB | C-u TAB
## Global cycling

,-> OVERVIEW -> CONTENTS -> SHOW ALL --.
'--------------------------------------'

----------------------------------------
# add a start keyword: overview, content, showall to define the startup action
#+STARTUP: content
```

- jump between heading

```
C-c C-n ==> next heading
C-c C-p ==> previous heading
C-c C-f ==> next heading same level
C-c C-b ==> previous heading same level
C-c C-u ==> back to higher level heading
```

- structure editing

```
M-RET       ==> no use in evil
M-S-RET     ==> no use in evil
S-left/right==> list[ol<->ul] | heading[todo<->done]
S-up/down   ==> heading[#A<->#C]
M-left/right==> heading[level]
M-up/down   ==> list[up<->down] | heading [up<->down]
```

- Sparse trees

sparse trees for selectes information

```
C-c /
C-c /r
```

- Plain lists

```
# ul

+ list-1
+ list-2
  + sublist-1
  + sublist-2
+ list-3 :: desc

# ol

1. ol-1
2. ol-2

# checkbox
C-c C-c toggle checkbox
[%] and [/] can show process

+ [ ] task [%]
  + [ ] task-1
  + [ ] tsak-2
```

- Footnotes

```
This is a footnotes[fn:1]
...
[fn:1] Footenotes is ...

C-c C-x f ==> jump to the definition
C-c C-c   ==> jump between definition and reference
```

TABLES
---

```
|h-1|h-2|h-3|
|- "==> now TAB would autocomplete it"
| "==> now TAB would autocomplete it"

"TAB/up/down/left/right" move cursor 
C-c - ==> insert a horizontal line below current row
C-c ^ ==> sort the table line in the region
```

HYPERLINKS
---

```
# link format
[[link][description]]
[[link]]

C-c C-l ==> edit invisible link

# internal link

[[#my-custom-id]]

[[my target]] ==> find <<my target>>
[[job]] ==> find <<job>>

# external links

http://www.google.com
file:/home/xx/j.jpg
/home/xx/j.jpg
file:papers/last.pdf
file:projects.org
...
```

- handling links

```
C-c l
C-c C-l ==> insert a link
C-c C-l ==> edit link
```

- target links

```
[[file:~/code/main.c::255]]
[[file:~/xx.org::my target]]
[[file:~/xx.org::#my-custom-id]]
```

TODO Items
---

- using todo states

```
C-c C-t         ==> rotate todo states
S-left/right    ==> simply cycling
C-c/t           ==> view todo items in a sparse tree
C-c a t         ==> show global todo list
```

- multi-state workflows

```
(set org-todo-keywords
    '((sequence "TODO" "FEEDBACK" "VERIFY" "|" "DONE" "DELEGATED")))
...more...
```

- progress logging


TAGS
---

PROPERTIES
---

DATES AND TIMES
---

CAPTURE-REFILE-ARCHIVE
---

EXPORTING
---

PUBLISHING
---

WORKING WITH SOURCE CODE
---

MISCELLANEOUS
---



