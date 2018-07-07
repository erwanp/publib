# -*- coding: utf-8 -*-
"""
publib
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from .main import set_style, fix_style
from .tools.colors import colors, keep_color, get_next_color
from .tools.tools import reset_defaults, regenerate_fonts

def __get_version__():
    from os.path import join, dirname
    # Read version number from file
    with open(join(dirname(__file__), '__version__.txt')) as version_file:
        __version__ = version_file.read().strip()
    return __version__

__version__ = __get_version__()