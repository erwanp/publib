# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:04:31 2018

@author: erwan
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib as mpl
from publib.tools.tools import regenerate_fonts

def fix_bold_TimesNewRoman():
    ''' For some reason when using Times New Roman it appears bold
    This fixes it
    
    References
    ----------
    
    https://stackoverflow.com/questions/33955900/matplotlib-times-new-roman-appears-bold
    
    '''
    
    try:
        del mpl.font_manager.weight_dict['roman']
    except KeyError:
        pass
    finally:
        regenerate_fonts()

