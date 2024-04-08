# -*- coding: utf-8 -*-
"""

"""


from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib.pyplot as plt

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



def keep_color(ax=None):
    ''' Keep the same color for the same graph. 
    Warning: due to the structure of Python iterators I couldn't help but
    iterate over all the cycle twice. One first time to get the number of elements
    in the cycle, one second time to stop just before the last. And this still 
    only works assuming your cycle doesn't contain the object twice

    Note: when setting color= it looks like the color cycle state is not called

    TODO: maybe implement my own cycle structure 
    
    .. warning::
        only works if all colors in a cycle are unique
    '''

    if ax is None:
        ax = plt.gca()

    i = 1  # count number of elements
    next_color = ax._get_lines.get_next_color()
    a = ax._get_lines.get_next_color()     # a is already the next next color.
    # do a full cycle :
    while(a != next_color):
        i += 1
        a = ax._get_lines.get_next_color()
    print("guessed that cycle has size ", i)
    # We want a-1 to show up on next call to next. So a-2 must be set now
    for j in range(i - 2):
        ax._get_lines.get_next_color()

    print("Expected color is ", next_color)

    return None


def get_next_color(ax=None, nonintrusive=True):
    ''' Return the next color to be used in the given color cycle. 
    
    Warning: due to the structure of Python iterators I couldn't help but
    iterate over all the color cycle once. 

    If nonintrusive is True, then leave the color cycle in the same state as 
    before    

    .. warning::
        only works if all colors in a cycle are unique
    '''

    if ax is None:
        ax = plt.gca()

    i = 1  # count number of elements
    next_color = ax._get_lines.get_next_color()
    a = ax._get_lines.get_next_color()     # a is already the next next color.
    # do a full cycle :
    while(a != next_color):
        i += 1
        a = ax._get_lines.get_next_color()

    if nonintrusive:
        # We want a-1 to show up on next call to next. So a-2 must be set now
        for j in range(i - 1):
            ax._get_lines.get_next_color()

    return next_color
