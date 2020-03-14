# XPATH 

## XPATH TERMINOLOGY

**SEVEN KIND OF NODES:**

- element
- attribute
- text
- namespace
- processing-instruction
- comment
- document nodes

**ATOMIC VALUES**

nodes with no children or parent

*Items* are atomic values or nodes

**RELATIONSHIP OF NODES**

- parent
- children
- siblings
- ancestors
- descendants

## XPATH SYNATX

**SELECTING NODES**

|EXPRESSION|DESCRIPTION|
|----------|-----------|
|`nodename`|selects all nodes withs the name "nodename"|
|`/`|selects from the root node|
|`//`|selects nodes in the document from the current node that match the selection no matter where they are|
|`.`|select the current node|
|`..`|selects the parent of th document|
|`@`|selects all attributes|

**PREDICATES**

|EXPRESSION|DESCRIPTION|
|----------|-----------|
|`/bookstore/book[1]`|selects the first book element that is the child of bookstore element|
|`/bookstore/book[last()]`|selects the last book element that is the child of bookstore element|
|`/bookstore/book[last()-1]`|selects the last second book element that is the child of bookstore element|
|`/bookstore/book[postition()<3]`|selects the first two book element that is the child of bookstore element|
|`//title[@lang]`|selects all the title that has a "lang" attribute|
|`/bookstore/book[price>35.00]`|selects all the book element that price is less than 35.00|
|`/bookstore/book[price>35.00]/title`|slects all the title element of book element that the priceis more than 35.00|

**SELECT UNKNOWN  NODES**

|WILDCARD|DESCRIPTION|
|-------|------------|
|`*`|matches any element nodes|
|`@*`|matches any attribute node|
|`node()`|match any node of any kind|

**SELECT SEVERAL PATHS**

|PATH EXPRESSION|RESULTS|
|---------------|-------|
|`//book/title &#124; //book/price`|selects all the title AND price elements of all book elements|
|`//title &#124; //price`|selects all the title AND price elements in the documnet|
|`/bookstore/book/title &#124; //price`|selects all the title elements of the  book element of bookstore element AND  all the price elements in the documnets|

**xpath axes**

axis defines a node-set relative to the current node

|axisname|result|
|--------|------|
|`ancestor`|selects all the ancestors(parent, grandparent) of the current node|
|`ancestor-or-self`|selects all the ancestors(parent, grandparent) of the current node and the current node|
|`attribute`|selects all the attribute of the current node|
|`child`|selects all children of the current node|
|`descendant`|selects all descendants(children,grandchildren,etc) of the current node|
|`descendant-or-self`|selects all descendants(children,grandchildren,etc) of the current node and the current node it self|
|`following`|selects everythong in the document after the closing tag of the  current node|
|`following-sibling`|selects all siblings after the current node|
|`namespace`|selects all namespace of the current node|
|`parent`|selects the parent of the current node|
|`preceding`|selects all nodes thata appear before the current node in the document, except ancestors, attribute nodes and namespace nodes|
|`preceding-sibling`|selects all siblings before the current node|
|`self`|selects the current node|

**location path expression**

- absolute location: `/step/step`
- relative location: `step/step/`

> a step consist of
> - an axis(defines the tree-relativeship between the selected node and the current node.)
> - a node-test(idetified a node within an axis)
> - zero or more predicates(to further refine the selected node-set)

**syntax for a location step**

```
axisname::nodetest[predicate]
```

**examples**

|example|result|
|-------|------|
|`child::book`|selects all book nodes that are child of the current node|
|`attribute::lang`|selects the lang attribut of the current node|
|`child::*`|selects all elements of children of th current node|
|`attribute::*`|selects all the attribute of the current node|
|`child::text()`|selects all text node children of the current node|
|`child::node()`|selects all children of the current node|
|`descendant::book`|selects all book descendants of the current node|
|`ancenstor::book`|selects all ancestors of the current node|
|`ancestor-or-self::book`|selects all ancestors of the current node and itself if it is a book node|
|`child::*/child::price`|selects all price grandchildren of the current node|
