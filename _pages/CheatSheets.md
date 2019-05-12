---
permalink: /cheatsheets_markdown/
title: Markdown Style Guide
---

## Core Information to get started:
* [Python](/cheatsheets/python.png)
* [Python Data Science](/cheatsheets/pythonfordatascience.pdf)

* [Numpy](/cheatsheets/Numpy_Python_Cheat_Sheet.pdf)
* [Matplotlib](/cheatsheets/Python_Matplotlib_cheat_sheet.pdf)
* [Pandas](/cheatsheets/Pandas_Cheat_Sheet.pdf)

* [Conda](/cheatsheets/conda-cheatsheets.pdf)
* [Anaconda](/cheatsheets/Anaconda_Cheatsheet.pdf)

* [Markdown](/cheatsheets/markdown-cheatsheet-online.pdf)
 



## Markdown Syntax used in this Blog  
### Mainly for my reference as I can't remember anything

[View the markdown used to create this post](https://raw.githubusercontent.com/barryclark/www.jekyllnow.com/gh-pages/_posts/2014-6-19-Markdown-Style-Guide.md).

This is a paragraph, it's surrounded by whitespace. Next up are some headers, they're heavily influenced by GitHub's markdown style.

## Header 2 (H1 is reserved for post titles)##

### Header 3

#### Header 4
 
A link to [Jekyll Now](http://github.com/barryclark/jekyll-now/). A big literal link <http://github.com/barryclark/jekyll-now/>
  
* A bulletted list
- alternative syntax 1
+ alternative syntax 2
  - an indented list item

1. An
2. ordered
3. list

Inline markup styles: 

- _italics_
- **bold**
- `code()` 
 
> Blockquote
>> Nested Blockquote 
 
Syntax highlighting can be used by wrapping your code in a liquid tag like so:

{{ "{% highlight javascript " }}%}  
/* Some pointless Javascript */
var rawr = ["r", "a", "w", "r"];
{{ "{% endhighlight " }}%}  

creates...

{% highlight javascript %}
/* Some pointless Javascript */
var rawr = ["r", "a", "w", "r"];
{% endhighlight %}
 
Use two trailing spaces  
on the right  
to create linebreak tags  
 
Finally, horizontal lines
 
----
****