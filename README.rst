Publib
======

Description
-----------

Produce publication-level quality images on top of Matplotlib, with a
simple call to a couple functions at the start and end of your script.

`Project GitHub page <https://github.com/erwanp/publib>`__

For similar librairies, see
`seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`__, which also
add neat high-end API to Matplotlib function calls, and the Matplotlib
default `style
feature <http://matplotlib.org/users/style_sheets.html>`__

Install
-------

::

    pip install publib

Use
---

At the beginning of the script, call:

.. code:: python

    set_style()

After each new axe is plotted, call:

.. code:: python

    fix_style()

Note that importing publib will already load the basic style.

A few more styles ('poster', 'article', etc.) can be selected with the
function ``set_style()``

Because some matplotlib parameters cannot be changed before the lines
are plotted, they are called through the function ``fix_style()`` which:

-  changes the minor ticks

-  remove the spines

-  turn the legend draggable by default

Examples
--------

.. code:: python

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl

A default Matplotlib plot:

.. code:: python

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

.. figure:: https://github.com/erwanp/publib/blob/master/docs/mpl_default.png
   :alt: mpl\_defaults.png

   mpl\_defaults.png

And now the same code with the two new lines calling the publib
functions

.. code:: python

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

.. figure:: https://github.com/erwanp/publib/blob/master/docs/publib_article.png
   :alt: publib\_article.png

   publib\_article.png

Run the \_test() routine in publib.py for more examples.

Changes
-------

-  0.1.9: added talk and OriginPro style

-  0.1.8 : fixed deprecation error messages

-  0.1.7 : default fonts to Times in article

-  0.1.6 : improve Readme

-  0.1.5 : changed those buff\_style functions in fix\_style

*Erwan Pannier - EM2C Laboratory, CentraleSupélec / CNRS UPR 288*
