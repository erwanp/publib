# -*- coding: utf-8 -*-
"""

"""

from publib import set_style
from publib.tools import colors, keep_color, get_next_color

import matplotlib.pyplot as plt


def test_keep_color(*args, **kwargs):
    ''' Make sure keep_color reset the color cycle so that
    the next color is the same as the previous '''

    plt.ion()    # force interactive mode (so we're not stuck when run from terminal)

    plt.figure()
    plt.plot(0,1,'o')
    
    current_color = get_next_color()
    
    plt.plot(1,1,'o')
    
    keep_color()
    assert get_next_color() == current_color
    
    

if __name__ == '__main__':
    
    test_keep_color()
    

