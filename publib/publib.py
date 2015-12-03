# -*- coding: utf-8 -*-
"""
@author: Erwan

Produce publication-level quality images on top of Matplotlib

For similar librairies, see seaborn, which also add neat high-end API to 
Matplotlib function calls.  

--------
Use
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import publib
>>> a = np.linspace(0,6.28)
>>> plt.plot(a,np.cos(a))
>>> plt.show()

>>> publib.set_style('article')
>>> plt.plot(a,a**2)
>>> publib.buff_style('article')
>>> plt.show()

"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import os

style_params={
    'default':{'clean_spines':True},
    'article':{'clean_spines':False},
    'poster': {'clean_spines':True},
    }

def set_style(style='default'):
    ''' 

    Parameters
    ----------    
    style: string
        'default', 'article', 'poster'
    
    Examples
    --------
    >>> set_style("article")

    '''
    
    mpl.style.use(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'stylelib',style+'.mplstyle'))
    
    return

def buff_style(style='default',ax=None,**kwargs):
    ''' 
    Add an extra formatting layer to an axe, that couldn't be changed directly 
    in matplotlib.rcParams or with styles. Apply this function to every axe 
    you created.
    
    Parameters
    ----------    
    ax: a matplotlib axe. 
        If None, the last axe generated is used 
    style: string
        one of the styles previously defined. It should match the style you 
        chose in set_style but nothing forces you to.
        
    Examples
    --------
    plb.set_style('poster')
    plt.plot(a,np.cos(a))
    plb.buff_style('poster')    
    
    
    '''
    
    params = style_params[style]
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
        
    return

set_style('default')        # whenever publib is imported

# %% Test routines

def _test():
    ''' Note : for some reason using latex will also apply to the plot showing
    the default behaviour of matplotlib (it seems that this parameter
    is retroactive
    '''
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    # %% Examples
    def example1():
        x = np.linspace(0,5,250)
        y = np.cos(x)**2+np.random.normal(scale=0.5,size=len(x))
        yav = np.cos(x)**2
        plt.figure()
        ax = plt.subplot()
        ax.plot(x,y,'o',label='normal distribution')
        ax.plot(x,yav,zorder=-1,label='average')
        plt.xlabel(r'$x$ $(\sum_{i=0}^\infty x_i=1250)$')
        plt.ylabel(r'$\cos^2 x$+noise background')
        plt.title(r'Matplotlib output with and without correction')
        plt.legend(loc='upper left')
        plt.show()
        return ax
        
    def example2():
        x = np.linspace(0,5,50)
        y = np.cos(x)**2+1*np.random.random(len(x))
        yerr = np.ones_like(y)*np.std(y)
        plt.figure()
        ax = plt.subplot()
        ax.errorbar(x,y,yerr=yerr,fmt='o',label='Draggable legend')
        plt.xlabel(r'$x$ $(\sum_{i=0}^\infty x_i=1250)$')
        plt.ylabel(r'$\cos^2 x$+noise background')
        plt.title(r'Matplotlib output with and without correction')
        leg = plt.legend(loc='upper left')        
        if leg: leg.draggable()
        plt.show()
        return ax

    def example3():
        x = np.linspace(0,5,10)
        y = np.cos(x)**2+0.1*np.random.random(len(x))
        yerr = np.ones_like(y)*np.std(y)
        plt.figure()
        ax = plt.subplot()
        ax.errorbar(x,y,yerr=yerr,marker='o',capsize=5, # example of use of capsize
                    label='scaled legend marker size') 
        plt.xlabel(r'$x$ $(\sum_{i=0}^\infty x_i=1250)$')
        plt.ylabel(r'$\cos^2 x$+noise background')
        plt.title(r'Matplotlib output with and without correction')
        plt.legend(markerscale=1.3)
        plt.show()
        
        return ax
        
    
    # %% Plot them
    plt.close('all')    
    for example in [example1,example2]:
    
        # Default plot 
        mpl.rcParams.update(mpl.rcParamsDefault)
        example()
        
        # The two functions to apply to format a graph correctly
        set_style('default')
        ax=example()
        buff_style('default')
        
    return None

if __name__ == '__main__':
    _test()
