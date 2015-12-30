Publib
======

Produce publication-level quality images on top of Matplotlib

For similar librairies, see `seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`__, which also add neat high-end API to 
Matplotlib function calls.


Use
===

At the beginning of the script, call:

.. code-block:: python

    set_style()
	
After each new axe is plotted, call:

.. code-block:: python

    fix_style()

Note that importing publib will already load the default style. 

A couple more styles ('poster', 'article') can be selected with the function
set_style()

Because some matplotlib parameters cannot be changed before the lines are 
plotted, they are called through the function fix_style() which:

- changes the minor ticks

- remove the spines

- turn the legend draggable by default

Examples
========

.. code:: python

	#!/usr/bin/env python
	import numpy as np
	import matplotlib.pyplot as plt
	import publib
	a = np.linspace(0,6.28)
	plt.plot(a,np.cos(a))   # plotted by publib 'default' style
	plt.show()

	publib.set_style('article')
	plt.plot(a,a**2)
	publib.fix_style('article')
	plt.show()
