---
permalink: /cheatsheets_markdown/
title: Markdown Style Guide
---

## Core Information to get started 
### All work by others, collected from around the web:

* [Probability](/cheatsheets/Probability_cheatsheet.pdf)
- [Probability](/cheatsheets/cheatsheet-probability.pdf)
* [Statistics](/cheatsheets/Statics_cheatsheet.pdf)
- [Statistics](/cheatsheets/cheatsheet-statistics.pdf)

* [Calculus](/cheatsheets/Calculus.pdf)
1. [ODEs](/cheatsheets/cheatsheet-first-ode.pdf)
2. [ODEs](/cheatsheets/cheatsheet-second-ode.pdf)

### Coding 
* [Command Line](https://ss64.com/nt/)
* [R](/cheatsheets/R_cheatsheet.png)
* [SQL](/cheatsheets/SQL.pdf)
* [Machine Learning Map](/cheatsheets/ml_map.png)
* [Markdown](/cheatsheets/markdown-cheatsheet-online.pdf)

### Python
* [Python Data Science](/cheatsheets/PythonForDataScience.pdf)

* [Numpy](/cheatsheets/Numpy_cheatsheet.pdf)
* [Matplotlib](/cheatsheets/Matplotlib_cheatsheet.pdf)
* [SciPy](/cheatsheets/scipy_cheatsheet.png)
* [Pandas](/cheatsheets/Pandas_cheatsheet.pdf)
- [Pandas](/cheatsheets/Pandas_Notes.pdf)

* [Conda](/cheatsheets/conda-cheatsheet.pdf)
* [Anaconda](/cheatsheets/Anaconda_CheatSheet.pdf)


 



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