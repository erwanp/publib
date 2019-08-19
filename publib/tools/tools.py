# -*- coding: utf-8 -*-
"""
Some tools and tips to fix common Matplotlib bugs
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib as mpl
from warnings import warn

def reset():
    
    warn(DeprecationWarning('reset replaced by reset_defaults'))
    
    return reset_defaults()
    
def reset_defaults():
    ''' Reset to Matplotlib defaults 
    
    See Also
    --------
    
    :func:`~publib.publib.set_style`
    :func:`~publib.publib.fix_style`

    '''
    
    mpl.rcdefaults()



def regenerate_fonts():
    ''' Regenerate Matplotlib font cache 
    
    References
    ----------
    
    https://bastibe.de/2016-05-30-matplotlib-font-cache.html
    
    '''
    
    mpl.font_manager._rebuild()
    
def list_font_names():
    ''' List ttf font names '''
    
    return sorted([f.name for f in mpl.font_manager.fontManager.ttflist])

def list_font_files():
    ''' List ttf font names '''
    
    return {f.name:f.fname for f in sorted(mpl.font_manager.fontManager.ttflist, 
                                           key=lambda x: x.name)}