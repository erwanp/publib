# -*- coding: utf-8 -*-
"""
@author: Erwan Pannier

Produce publication-level quality images on top of Matplotlib

For similar librairies, see seaborn, which also add neat high-end API to 
Matplotlib function calls.


Description
--------

Use::
    
    set_style()       # at the beginning of the script
    ...
    fix_style()       # after each new axe is plotted

Note that importing publib will already load the basic style by default. 

A couple more styles ('poster', 'article', 'origin') can be selected with the 
function :func:`~publib.publib.set_style`

Because some matplotlib parameters cannot be changed before the lines are 
plotted, they are called through the function fix_style() which:
- changes the minor ticks
- remove the spines
- turn the legend draggable by default

Examples
--------

    import numpy as np
    import matplotlib.pyplot as plt
    import publib
    a = np.linspace(0,6.28)
    plt.plot(a,np.cos(a))   # plotted by publib 'basic' style
    plt.show()
    
    publib.set_style('article')
    plt.plot(a,a**2)
    publib.fix_style('article')
    plt.show()


Notes
-----

Known issues:

If fonts (ex: Times New Roman) appear to be bold, you may need Matplotlib to regenerate
its font library cache (delete ~/.matplotlib/fontCache)

See dedicated Stackoverflow::

    https://stackoverflow.com/questions/33955900/matplotlib-times-new-roman-appears-bold
    
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from os.path import dirname, join
from six import string_types

style_params = {
    'basic': {'clean_spines': True,
              'draggable_legend': True,
              'draggable_text': True,
              'tight_layout': True,
              'labelpad': 10,
              },
    'article': {'clean_spines': False,
                },
    'article_s': {'clean_spines': False,
                  'labelpad': 5,
                  'spine_linewidth': 0.5,
                  },
    'poster': {},
    'B&W': {},
    'talk': {'clean_spines': False},
    'origin': {'clean_spines': False,
               },
    'latex': {},
}

def set_style(style='basic', **kwargs):
    ''' Changes Matplotlib basic style to produce high quality graphs. Call 
    this function at the beginning of your script. You can even further improve
    graphs with a call to :py:func:`~publib.main.fix_style` at the end of your script.

    Parameters
    ----------    
    style: string
        'basic', 'article', 'poster', 'B&W', 'talk', 'origin', 'latex'``

    kwargs: dict of rcParams
        add Matplotlib rcParams    

    Examples
    --------
    >>> set_style('article')

    >>> set_style('poster',**{'lines.linewidth':2})
    
    See Also
    --------
    
    :func:`~publib.publib.fix_style`,
    :func:`~publib.tools.tools.reset_defaults`,
    :func:`~publib.tools.tools.regenerate_fonts`

    '''

    style = _read_style(style)

    # Add basic style as the first style
    if style[0] != 'basic':
        style = ['basic'] + style

    # Apply all styles
    for s in style:
        _set_style(s, **kwargs)


def _set_style(style, **kwargs):

    stl = _get_style(style)

    if not os.path.exists(stl):
#        avail = os.listdir()
        avail = [f.replace('.mplstyle', '') for f in os.listdir(
            _get_lib()) if f.endswith('.mplstyle')]
        raise ValueError('{0} is not a valid style. '.format(stl) +
                         'Please pick a style from the list available in ' +
                         '{0}: {1}'.format(_get_lib(), avail))

    mpl.style.use(stl)

    for k in kwargs:
        mpl.rcParams[k] = kwargs[k]

    return


def fix_style(style='basic', ax=None, **kwargs):
    ''' 
    Add an extra formatting layer to an axe, that couldn't be changed directly 
    in ``matplotlib.rcParams`` or with styles. Apply this function to every axe 
    you created.

    Parameters
    ----------    
    ax: a matplotlib axe. 
        If None, the last axe generated is used 
    style: string or list of string
        ``['basic', 'article', 'poster', 'B&W', 'talk', 'origin', 'latex']``
        one of the styles previously defined. It should match the style you 
        chose in set_style but nothing forces you to.
    kwargs: dict
        edit any of the style_params keys. ex::
            
        >>> tight_layout=False

    Examples
    --------
    
    ::
        
        from publib import set_style, fix_style
        set_style('poster')
        plt.plot(a,np.cos(a))
        fix_style('poster',**{'draggable_legend':False})    
    
    See Also
    --------
    
    :func:`~publib.publib.set_style`, 
    :func:`~publib.tools.tools.reset_defaults`

    '''

    style = _read_style(style)

    # Apply all styles
    for s in style:
        if not s in style_params.keys():
            raise ValueError('{0} is not a valid style. '.format(s)+
                    'Please pick a style from the following: {0}. '.format(style_params.keys())+\
                    'Or update `style_params` in publib.main.py')

    _fix_style(style, ax, **kwargs)


def _fix_style(styles, ax=None, **kwargs):

    # Start with basic params
    params = style_params['basic']

    # Apply all styles params
    for s in styles:
        for p, v in style_params[s].items():
            params[p] = v

    # User defined params:
    for k in kwargs:
        params[k] = kwargs[k]

    if ax is None:
        try:
            ax = plt.gca()
        except:
            raise ValueError('Please select an axis')

    if 'spine_linewidth' in params.keys():
        for spine in ['left', 'bottom', 'right', 'top']:
            ax.spines[spine].set_linewidth(params['spine_linewidth'])

    if params['clean_spines']:
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

    # Tight layout
    if params['tight_layout']:
        plt.tight_layout()

    # Labelpads, offsets, etc.
    ax.xaxis.labelpad = params['labelpad']
    ax.yaxis.labelpad = params['labelpad']

    titleoffset = 1.05
    ax.title.set_y(titleoffset)

    # Minorticks:
    if not ax.get_xscale() == 'log':
        minor_locatorx = mpl.ticker.AutoMinorLocator(2)
        ax.xaxis.set_minor_locator(minor_locatorx)
    if not ax.get_yscale() == 'log':
        minor_locatory = mpl.ticker.AutoMinorLocator(2)
        ax.yaxis.set_minor_locator(minor_locatory)

    # Render legend draggable:
    if params['draggable_legend']:
        l = ax.get_legend()
        if not l is None:
            try:
                l.set_draggable(True)
            except AttributeError: # Deprecated method
                l.draggable(True)

    if params['draggable_text']:
        for t in ax.get_children():
            if type(t) == mpl.text.Annotation:
                t.draggable(True)

    return


def _read_style(style):
    ''' Deal with different style format (str, list, tuple)
    
    Returns
    -------
    
    style: list
        list of styles
    '''

    if isinstance(style, string_types):
        style = [style]
    else:
        style = list(style)

    return style


def _get_style(style):
    ''' Get absolute path of style file '''
    return join(_get_lib(),'{0}.mplstyle'.format(style))

def _get_lib():
    ''' Get absolute path of styles '''
    return join(dirname(os.path.realpath(__file__)),'stylelib')

# %% On start-up

set_style('basic')        # whenever publib is imported



if __name__ == '__main__':
    from test.test_functions import run_testcases
    run_testcases()
