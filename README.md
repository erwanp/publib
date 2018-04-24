[![PyPI version](https://badge.fury.io/py/publib.svg)](https://badge.fury.io/py/publib)
[![Tests](https://img.shields.io/travis/erwanp/publib.svg)](https://travis-ci.org/erwanp/publib)
[![Code coverage](https://codecov.io/gh/erwanp/publib/branch/master/graph/badge.svg)](https://codecov.io/gh/erwanp/publib)

# Publib

## Description

Produce publication-level quality images on top of Matplotlib, with a 
simple call to a couple functions at the start and end of your script. 

[Project GitHub page](https://github.com/erwanp/publib)

For similar librairies, see
[seaborn](http://stanford.edu/~mwaskom/software/seaborn/), which also
add neat high-end API to Matplotlib function calls, and the Matplotlib 
default [style feature](http://matplotlib.org/users/style_sheets.html)

## Install

```
pip install publib
```

## Use

At the beginning of the script, call:

``` {.sourceCode .python}
set_style()
```

After each new axe is plotted, call:

``` {.sourceCode .python}
fix_style()
```

Note that importing publib will already load the basic style.

A few more styles ('poster', 'article', etc.) can be selected with the
function `set_style()`

Because some matplotlib parameters cannot be changed before the lines
are plotted, they are called through the function `fix_style()` which:

-   changes the minor ticks

-   remove the spines

-   turn the legend draggable by default

## Examples

``` {.sourceCode .python}
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
```

A default Matplotlib plot:

``` {.sourceCode .python}
mpl.rcdefaults()

x = np.linspace(0,5,250)
y = np.cos(x)**2+np.random.normal(scale=0.5,size=len(x))
yav = np.cos(x)**2
plt.figure()
ax = plt.subplot()
ax.plot(x,y,'o',label='normal distribution')
ax.plot(x,yav,zorder=-1,label='average')
plt.xlabel(r'$x$')
plt.ylabel(r'$\cos^2 x$+noise')
plt.title('matplotlib')
plt.legend(loc='upper left')
plt.ylim((-1.5,3.5))
plt.show()
plt.savefig('mpl_default.png')
```

![mpl_defaults.png](https://github.com/erwanp/publib/blob/master/docs/mpl_default.png)

And now the same code with the two new lines calling the 
publib functions

``` {.sourceCode .python}
from publib import set_style, fix_style
set_style('article')        # before the first plot

x = np.linspace(0,5,250)
y = np.cos(x)**2+np.random.normal(scale=0.5,size=len(x))
yav = np.cos(x)**2
plt.figure()
ax = plt.subplot()
ax.plot(x,y,'o',label='normal distribution')
ax.plot(x,yav,zorder=-1,label='average')
plt.xlabel(r'$x$')
plt.ylabel(r'$\cos^2 x$+noise')
plt.title('article')
plt.legend(loc='upper left')
plt.ylim((-1.5,3.5))

fix_style('article')  # after the axe has been created

plt.show()
plt.savefig('publib_article.png')
```

![publib_article.png](https://github.com/erwanp/publib/blob/master/docs/publib_article.png)

Run the test() routines in `publib.test` for more examples. 


## Tools

The publib.tools module include independant functions to fix some common matplotlib bugs, 
or include extra features. They're usually glanced from somewhere on the web. Proper  
referencing is made in the function docstrings. 

See for instance:

- `publib.tools.reset`: reset Matplotlib defaults 

- `publib.tools.fix_bold_TimesNewRoman`: fix Times New Roman font appearing bold. See 
[StackOverflow](https://stackoverflow.com/questions/33955900/matplotlib-times-new-roman-appears-bold)


See [tools.py](https://github.com/erwanp/publib/blob/master/publib/tools/tools.py) 
for more details

## Changes

- 0.2.2: added tools

- 0.1.9: added talk and OriginPro style 

- 0.1.8 : fixed deprecation error messages

- 0.1.7 : default fonts to Times in article

- 0.1.6 : improve Readme

- 0.1.5 : changed those buff_style functions in fix_style 

*Erwan Pannier - EM2C Laboratory, CentraleSupélec / CNRS UPR 288*

