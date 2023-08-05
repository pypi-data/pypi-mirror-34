'''
Plot up stuff with colormaps.
'''

import sys

import numpy as np
import matplotlib as mpl


if sys.version_info > (3,):
    _string_types = (str, np.str_, np.unicode_)
else:
    _string_types = (basestring, np.str_, np.unicode_)


def print_colormaps(cmaps, N=256, returnrgb=True, savefiles=False):
    '''Print colormaps in 256 RGB colors to text files.

    :param returnrgb=False: Whether or not to return the rgb array. Only makes sense to do if print one colormaps' rgb.

    '''

    rgb = []

    for cmap in cmaps:

        rgbtemp = cmap(np.linspace(0, 1, N))[np.newaxis, :, :3][0]
        if savefiles:
            np.savetxt(cmap.name + '-rgb.txt', rgbtemp)
        rgb.append(rgbtemp)

    if returnrgb:
        return rgb


def get_dict(cmap, N=256):
    '''Change from rgb to dictionary that LinearSegmentedColormap expects.
    Code from https://mycarta.wordpress.com/2014/04/25/convert-color-palettes-to-python-matplotlib-colormaps/
    and http://nbviewer.ipython.org/github/kwinkunks/notebooks/blob/master/Matteo_colourmaps.ipynb
    '''

    x = np.linspace(0, 1, N)  # position of sample n - ranges from 0 to 1

    rgb = cmap(x)

    # flip colormap to follow matplotlib standard
    if rgb[0, :].sum() < rgb[-1, :].sum():
        rgb = np.flipud(rgb)

    b3 = rgb[:, 2]  # value of blue at sample n
    b2 = rgb[:, 2]  # value of blue at sample n

    # Setting up columns for tuples
    g3 = rgb[:, 1]
    g2 = rgb[:, 1]

    r3 = rgb[:, 0]
    r2 = rgb[:, 0]

    # Creating tuples
    R = list(zip(x, r2, r3))
    G = list(zip(x, g2, g3))
    B = list(zip(x, b2, b3))

    # Creating dictionary
    k = ['red', 'green', 'blue']
    LinearL = dict(zip(k, [R, G, B]))

    return LinearL


def cmap(rgbin, N=256):
    '''Input an array of rgb values to generate a colormap.

    :param rgbin: An [mx3] array, where m is the number of input color triplets which
         are interpolated between to make the colormap that is returned. hex values
         can be input instead, as [mx1] in single quotes with a #.
    :param N=10: The number of levels to be interpolated to.

    '''

    # rgb inputs here
    if not isinstance(rgbin[0], _string_types):
        # normalize to be out of 1 if out of 256 instead
        if rgbin.max() > 1:
            rgbin = rgbin/256.

    cmap = mpl.colors.LinearSegmentedColormap.from_list('mycmap', rgbin, N=N)

    return cmap


def lighten(cmapin, alpha):
    '''Lighten a colormap by adding alpha < 1.

    :param cmap: A colormap object, like cmocean.cm.matter.
    :param alpha: An alpha or transparency value to assign the colormap. Alpha
        of 1 is opaque and of 1 is fully transparent.

    Outputs resultant colormap object.

    This will lighten the appearance of a plot you make using the output
        colormap object. It is also possible to lighten many plots in the
        plotting function itself (e.g. pcolormesh or contourf).
    '''

    # set the alpha value while retaining the number of rows in original cmap
    return cmap(cmapin(np.linspace(0,1,cmapin.N), alpha))
