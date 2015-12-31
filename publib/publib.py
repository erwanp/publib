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

Note that importing publib will already load the default style. 

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
    plt.plot(a,np.cos(a))   # plotted by publib 'default' style
    plt.show()
    
    publib.set_style('article')
    plt.plot(a,a**2)
    publib.fix_style('article')
    plt.show()

"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import os

style_params={
    'basic':{'clean_spines':True,
               'draggable_legend':True,
               'tight_layout':True
               },
    'article':{'clean_spines':False,
               },
    'poster':{},
    'B&W':{}
    }

def set_style(style='basic'):
    ''' Changes Matplotlib basic style to produce high quality graphs. Call 
    this function at the beginning of your script. You can even further improve
    graphs with a call to fix_style at the end of your script.

    Parameters
    ----------    
    style: string
        'basic', 'article', 'poster', 'B&W'
    
    Examples
    --------
    >>> set_style("article")

    '''
    
    if type(style)==str:
        style = [style]

    # Add basic style as the first style
    if style[0] != 'basic':
        style = ['basic']+style
    
    # Apply all styles
    for s in style:
        _set_style(s)
        
def _set_style(style):
    
    stl = _get_style(style)

    if not os.path.exists(stl):
        raise ValueError('Please pick a style from the list available:',style_params.keys())
    
    mpl.style.use(stl)
        
    return

def buff_style(*args):
    ''' Deprecated. Use fix_style '''
    from warnings import warn
    warn('buff_style deprecated. Please use fix_style')
    return fix_style(*args)

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
        ['basic', 'article', 'poster', 'B&W'] 
        one of the styles previously defined. It should match the style you 
        chose in set_style but nothing forces you to.
    kwargs: dict
        edit any of the style_params keys. 
        
    Examples
    --------
    plb.set_style('poster')
    plt.plot(a,np.cos(a))
    plb.fix_style('poster',{'draggable_legend':False})    
    
    '''
    
    if type(style)==str:
        style = [style]
        
    # Apply all styles
    for s in style:
            
        if not s in style_params.keys():
            raise ValueError('Please pick a style from the list available:',style_params.keys())
        
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
    
    if params['clean_spines']:
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
       
    # Tight layout
    if params['tight_layout']:
        plt.tight_layout()
    
    # Labelpads, offsets, etc.
    ax.xaxis.labelpad = 10
    ax.yaxis.labelpad = 10
    
    titleoffset = 1.05
    ax.title.set_y(titleoffset)
    
    # Minorticks:
    if not ax.get_xscale()=='log':
        minor_locatorx = mpl.ticker.AutoMinorLocator(2)
        ax.xaxis.set_minor_locator(minor_locatorx)
    if not ax.get_yscale()=='log':
        minor_locatory = mpl.ticker.AutoMinorLocator(2)
        ax.yaxis.set_minor_locator(minor_locatory)

    # Draggable legend:
    if params['draggable_legend']:
        l = ax.get_legend()
        if not l is None:
            l.draggable(True)
    
    return

def _get_style(style):
    ''' Get absolute path of style file '''
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'stylelib',style+'.mplstyle')


set_style('basic')        # whenever publib is imported

# %% Test routines

def _test():
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
        
        set_style(['article','B&W'])
        example('article',seed)
        fix_style(['article','B&W'])

        set_style('poster')
        example('poster',seed)
        fix_style('poster')

        # Default plot 
        mpl.style.use('classic')
        example('matplotlib',seed)
        
        mpl.style.use('ggplot')
        example('ggplot',seed)
        
    return None

if __name__ == '__main__':
    _test()
