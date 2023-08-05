'''
cmocean is a package to help standardize colormaps for commonly-plotted
oceanographic properties.

See README.md for an overview on instructions.
'''

from __future__ import absolute_import

# from cmocean import *
from . import cm, tools, data

__all__ = ['cm',
           'tools',
           'plots',
           'data']

__authors__ = ['Kristen Thyng <kthyng@tamu.edu>']

__version__ = "1.2"
