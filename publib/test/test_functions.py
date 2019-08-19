# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:26:37 2018

@author: erwan

-------------------------------------------------------------------------------


"""

from __future__ import absolute_import, print_function

from publib import set_style, fix_style
from publib.tools.tools import reset_defaults, regenerate_fonts
from publib.tools.fix import fix_bold_TimesNewRoman
import matplotlib as mpl

# %% Test routines

def test_routines(**kwargs):
    ''' Test that functions dont crash
    
    No Assert test is currently implemented
    
    Notes
    -----
    
    for some reason using latex will also apply to the plot showing
    the default behaviour of matplotlib (it seems that this parameter
    is retroactive
    '''

    import numpy as np
    import matplotlib.pyplot as plt

    # %% Examples
    def example1(title, seed):
        np.random.seed(seed)
        x = np.linspace(0, 5, 250)
        y = np.cos(x)**2 + np.random.normal(scale=0.5, size=len(x))
        yav = np.cos(x)**2
        plt.figure()
        ax = plt.subplot()
        ax.plot(x, y, 'o', label='normal distribution')
        ax.plot(x, yav, zorder=-1, label='average')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$\cos^2 x$+noise')
        plt.title(title)
        plt.legend(loc='upper left')
        plt.ylim((-1.5, 3.5))
        plt.show()
        return ax

#    def example2(title, seed):
#        np.random.seed(seed)
#        x = np.linspace(0, 5, 50)
#        y = np.cos(x)**2 + 1 * np.random.random(len(x))
#        yerr = np.std(y, axis=0)
#        plt.figure()
#        ax = plt.subplot()
#        ax.errorbar(x, y, yerr=yerr, fmt='o',
#                    label='new legends are draggable by default')
#        plt.xlabel(r'$x$')
#        plt.ylabel(r'$\cos^2 x$+noise')
#        plt.title(title)
#        plt.legend(loc='upper left')
#        plt.ylim((-1.5, 3.5))
#        plt.show()
#        return ax
#
#    def example3(title, seed):
#        np.random.seed(seed)
#        x = np.linspace(0, 5, 10)
#        y = np.cos(x)**2 + 0.1 * np.random.random(len(x))
#        yerr = np.std(y, axis=0)
#        plt.figure()
#        ax = plt.subplot()
#        ax.errorbar(x, y, yerr=yerr, marker='o', capsize=5,  # example of use of capsize
#                    label='scaled legend marker size')
#        plt.xlabel(r'$x$')
#        plt.ylabel(r'$\cos^2 x$+noise background')
#        plt.title(title)
#        plt.legend(markerscale=1.3)
#        plt.ylim((-1.5, 3.5))
#        plt.show()
#        return ax

    # %% Plot them
    plt.close('all')
    import time

    for example in [example1]:

        seed = int(time.time())
        mpl.rcdefaults()
        plt.ion()    # force interactive mode (so we're not stuck when run from terminal)

        set_style()
        example('basic', seed)
        fix_style()

        plt.pause(0.01)

        set_style('article')
        example('article', seed)
        fix_style('article')

        plt.pause(0.01)

#        set_style(['article','B&W'])
#        example('article',seed)
#        fix_style(['article','B&W'])

        set_style('poster', **{'lines.linewidth': 5})
        example('poster', seed)
        fix_style('poster', **{'draggable_legend': False})

        plt.pause(0.01)

        set_style(['origin'])
        example('OriginPro', seed)
        fix_style(['origin'])
        
        plt.pause(0.01)

        set_style(['origin', 'latex'])
        example('OriginPro + latex', seed)
        fix_style(['origin', 'latex'])
        
        plt.pause(0.01)

        # Default plot
        mpl.style.use('classic')
        example('matplotlib', seed)

        plt.pause(0.01)

        mpl.style.use('ggplot')
        example('ggplot', seed)

        plt.pause(0.01)

    return True



def test_tools():
    ''' Test publib tools are called properly '''
    
    regenerate_fonts
    reset_defaults()
    
    fix_bold_TimesNewRoman()

def run_testcases():
    
    test_routines()
    test_tools()

if __name__ == '__main__':
    run_testcases()