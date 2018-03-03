import numpy as np
#import pandas as pd

# -----------------------------
def wavedomain(tlim, xlim = np.NaN, ylim = np.NaN, zlim = np.NaN):
    """ Create a dictionary defining the boundaries
    of the domain. This can then be accessed by higher
    level functions to create visualizations on the
    specified domain.
    """

    domainBndry = {}
    domainBndry['xlim'] = xlim
    domainBndry['ylim'] = ylim
    domainBndry['zlim'] = zlim
    domainBndry['tlim'] = tlim

    return domainBndry

# -----------------------------
def wavegrid(tg, xg = np.NaN, yg = np.NaN, zg = np.NaN):

    domainGrid = {}
    domainGrid['tg'] = tg
    domainGrid['xg'] = xg
    domainGrid['yg'] = yg
    domainGrid['zg'] = zg
