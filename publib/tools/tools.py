# -*- coding: utf-8 -*-
"""
Some tools and tips to fix common Matplotlib bugs
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib as mpl

def reset():
    ''' Reset to Matplotlib defaults 
    
    See Also
    --------
    
    :func:`~publib.publib.set_style`
    :func:`~publib.publib.fix_style`

    '''
    
    mpl.rcdefaults()


def fix_bold_TimesNewRoman():
    ''' For some reason when using Times New Roman it appears bold
    This fixes it
    
    References
    ----------
    
    https://stackoverflow.com/questions/33955900/matplotlib-times-new-roman-appears-bold
    
    '''
    
    try:
        del mpl.font_manager.weight_dict['roman']
        mpl.font_manager._rebuild()
    except KeyError:
        pass

