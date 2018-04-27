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

