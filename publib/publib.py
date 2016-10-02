# -*- coding: utf-8 -*-
"""
@author: Erwan Pannier

Produce publication-level quality images on top of Matplotlib

For similar librairies, see seaborn, which also add neat high-end API to 
Matplotlib function calls.


--------
Use
    
    Call set_style() at the beginning of the script
    Call fix_style() after each new axe is plotted

Note that importing publib will already load the basic style by default. 

A couple more styles ('poster', 'article') can be selected with the function
set_style()

Because some matplotlib parameters cannot be changed before the lines are 
plotted, they are called through the function fix_style() which:
- changes the minor ticks
- remove the spines
- turn the legend draggable by default

--------
Examples

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

"""

from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from warnings import warn

style_params={
    'basic':{'clean_spines':True,
               'draggable_legend':True,
               'draggable_text':True,
               'tight_layout':True,
               'labelpad':10,
               },
    'article':{'clean_spines':False,
               },
    'article_s':{'clean_spines':False,
               'labelpad':5,
               'spine_linewidth':0.5,
               },
    'poster':{},
    'B&W':{},
    'talk':{'clean_spines':False},
    'origin':{'clean_spines':False,
               },
    }
    
# Colors available for import
colors = ['#5DA5DA',
           '#FAA43A',
           '#60BD68',
           '#F17CB0',
           '#B2912F',
           '#B276B2',
           '#DECF3F',
           '#F15854',
           '#4D4D4D']

def set_style(style='basic',**kwargs):
    ''' Changes Matplotlib basic style to produce high quality graphs. Call 
    this function at the beginning of your script. You can even further improve
    graphs with a call to fix_style at the end of your script.

    Parameters
    ----------    
    style: string
        'basic', 'article', 'poster', 'B&W', 'talk', 'origin'
    
    kwargs: dict of rcParams
        add Matplotlib rcParams    
    
    Examples
    --------
    >>> set_style('article')
    
    >>> set_style('poster',**{'lines.linewidth':2})

    '''
    
    style = _read_style(style)

    # Add basic style as the first style
    if style[0] != 'basic':
        style = ['basic']+style
    
    # Apply all styles
    for s in style:
        _set_style(s,**kwargs)
        
def _set_style(style,**kwargs):
    
    stl = _get_style(style)

    if not os.path.exists(stl):
#        avail = os.listdir()
        ValueError('{0} is not a valid style. '.format(style)+
                'Please pick a style from the list available:',style_params.keys())
        return
        
    mpl.style.use(stl)
    
    for k in kwargs:
        mpl.rcParams[k] = kwargs[k]
        
    return

def fix_style(style='basic',ax=None,**kwargs):
    ''' 
    Add an extra formatting layer to an axe, that couldn't be changed directly 
    in matplotlib.rcParams or with styles. Apply this function to every axe 
    you created.
    
    Parameters
    ----------    
    ax: a matplotlib axe. 
        If None, the last axe generated is used 
    style: string or list of string
        ['basic', 'article', 'poster', 'B&W','talk','origin'] 
        one of the styles previously defined. It should match the style you 
        chose in set_style but nothing forces you to.
    kwargs: dict
        edit any of the style_params keys. 
        
    Examples
    --------
    plb.set_style('poster')
    plt.plot(a,np.cos(a))
    plb.fix_style('poster',**{'draggable_legend':False})    
    
    '''
    
    style = _read_style(style)
        
    # Apply all styles
    for s in style:
            
        if not s in style_params.keys():
            avail = [f.replace('.mplstyle','') for f in os.listdir(_get_lib()) if f.endswith('.mplstyle')]
            raise ValueError('{0} is not a valid style. '.format(s)+
                            'Please pick a style from the list available in '+
                                '{0}: {1}'.format(_get_lib(),avail))
        
    _fix_style(style,ax,**kwargs)
        
def _fix_style(styles,ax=None,**kwargs):

    # Start with basic params
    params = style_params['basic']
    
    # Apply all styles params
    for s in styles:
        for p,v in style_params[s].items():
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
        for spine in ['left', 'bottom','right','top']:
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
    if not ax.get_xscale()=='log':
        minor_locatorx = mpl.ticker.AutoMinorLocator(2)
        ax.xaxis.set_minor_locator(minor_locatorx)
    if not ax.get_yscale()=='log':
        minor_locatory = mpl.ticker.AutoMinorLocator(2)
        ax.yaxis.set_minor_locator(minor_locatory)

    # Render legend draggable:
    if params['draggable_legend']:
        l = ax.get_legend()
        if not l is None:
            l.draggable(True)
            
    if params['draggable_text']:
        for t in ax.get_children():
            if type(t) == mpl.text.Annotation:
                t.draggable(True)
    
    return

def _read_style(style):
    ''' Deal with different style format (str, list, tuple)'''
    
    if type(style)==str:
        style = [style]
    else:
        style = list(style)
            
    return style

def _get_style(style):
    ''' Get absolute path of style file '''
    return os.path.join(_get_lib(),'{0}.mplstyle'.format(style))

def _get_lib():
    ''' Get absolute path of styles '''
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),'stylelib')

# %% On start-up

set_style('basic')        # whenever publib is imported


# %% Test routines

def _test(**kwargs):
    ''' Note : for some reason using latex will also apply to the plot showing
    the default behaviour of matplotlib (it seems that this parameter
    is retroactive
    '''

    import numpy as np
    import matplotlib.pyplot as plt
    
    # %% Examples
    def example1(title,seed):
        np.random.seed(seed)
        x = np.linspace(0,5,250)
        y = np.cos(x)**2+np.random.normal(scale=0.5,size=len(x))
        yav = np.cos(x)**2
        plt.figure()
        ax = plt.subplot()
        ax.plot(x,y,'o',label='normal distribution')
        ax.plot(x,yav,zorder=-1,label='average')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$\cos^2 x$+noise')
        plt.title(title)
        plt.legend(loc='upper left')
        plt.ylim((-1.5,3.5))
        plt.show()
        return ax
        
    def example2(title,seed):
        np.random.seed(seed)
        x = np.linspace(0,5,50)
        y = np.cos(x)**2+1*np.random.random(len(x))
        yerr = np.std(y,axis=0)
        plt.figure()
        ax = plt.subplot()
        ax.errorbar(x,y,yerr=yerr,fmt='o',label='new legends are draggable by default')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$\cos^2 x$+noise')
        plt.title(title)
        plt.legend(loc='upper left')
        plt.ylim((-1.5,3.5))
        plt.show()
        return ax

    def example3(title,seed):
        np.random.seed(seed)
        x = np.linspace(0,5,10)
        y = np.cos(x)**2+0.1*np.random.random(len(x))
        yerr = np.std(y,axis=0)
        plt.figure()
        ax = plt.subplot()
        ax.errorbar(x,y,yerr=yerr,marker='o',capsize=5, # example of use of capsize
                    label='scaled legend marker size') 
        plt.xlabel(r'$x$')
        plt.ylabel(r'$\cos^2 x$+noise background')
        plt.title(title)
        plt.legend(markerscale=1.3)
        plt.ylim((-1.5,3.5))
        plt.show()
        
        return ax
        
    
    # %% Plot them
    plt.close('all')    
    import time
    
    for example in [example1]:
        
        seed = int(time.time())    
        mpl.rcdefaults()
        
        set_style()
        example('basic',seed)
        fix_style()
        
        set_style('article')
        example('article',seed)
        fix_style('article')
        
#        set_style(['article','B&W'])
#        example('article',seed)
#        fix_style(['article','B&W'])

        set_style('poster',**{'lines.linewidth':5})
        example('poster',seed)
        fix_style('poster',**{'draggable_legend':False})

        set_style(['origin'])
        example('OriginPro',seed)
        fix_style(['origin'])

        # Default plot 
        mpl.style.use('classic')
        example('matplotlib',seed)
        
        mpl.style.use('ggplot')
        example('ggplot',seed)
        
    return None

if __name__ == '__main__':
    _test()
