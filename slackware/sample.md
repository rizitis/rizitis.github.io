---
layout: default
title: "Sample"
---
```
view code: https://github.com/rizitis/rizitis.github.io/tree/main/slackware/sample.md
```

# Header 1

This is a quote:

> We\'re living the future so
> the present is our past.

We can style words: *Italic*, **Bold** and `code span`.

## Header 2

List sample:

* Unordered list can use asterisks
- Or minuses
+ Or pluses

1. Ordered list item 1.
1. Ordered list item 2.

### Header 3

Table sample:

| Tables | Are | Cool | 
| ------------- |:-------------:| -----:| 
| col 3 is | right-aligned | $1600 | 
| col 2 is | centered | $12 | 
| zebra stripes | are neat | $1 |

#### Header 4

I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].

[1]: http://google.com/        'Google'
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    (MSN Search)

##### Header 5

* [markdown-it](https://github.com/markdown-it/markdown-it) for Markdown parsing
* [CodeMirror](http://codemirror.net/) for the awesome syntax-highlighted editor
* [highlight.js](http://softwaremaniacs.org/soft/highlight/en/) for syntax _highlighting_ in output code blocks
* [js-deflate](https://github.com/dankogai/js-deflate) for gzipping of data to make it fit in URLs

This is [an example] [id] reference-style link.

[id]: http://example.com/ 'Optional Title Here'

This is an image:
![A beautiful flower](../dita/flowers/images/Chrysanthemums.jpg "Chrysanthemum")

###### Header 6

XML sample:
<table>
   <tr>
      <td>Foo1</td>
      <td>Foo2</td>
   </tr>
   <tr>
      <td>Foo1</td>
      <td>Foo2</td>
   </tr>
</table>

---

**Task Lists**
- [x] Install Slackware
- [ ] Customize the kernel
- [ ] Try experimental package management tools


**Footnotes**
Here is a statement with a footnote.[^1]

---

**Blockquotes**
> "Slackware is about simplicity and elegance."
> — Patrick Volkerding

---
**Collapsible Sections (HTML)**
<details>
  <summary>Click to expand/collapse this section</summary>

  Here is some hidden content about advanced Slackware kernel tweaks. Add any lengthy instructions or additional notes here.

</details>

---

**Tables**
| Command          | Description                           |
|------------------|---------------------------------------|
| `slackpkg update`| Updates the list of available packages|
| `slackpkg install-new`| Installs new packages from the current list|
| `slackpkg upgrade-all` | Upgrades all installed packages  |


---

[![CLICK_ME](./images/slackware_logo_med.png)](https://www.youtube.com/watch?v=ikawDkK7Qns)

---
[^1]: This is the footnote explaining the statement.