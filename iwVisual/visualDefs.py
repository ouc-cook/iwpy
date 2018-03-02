import numpy as np
#import pandas as pd

def wavedomain(xlim, ylim = np.NaN, zlim = np.NaN, tlim = np.NaN):
    """ Create a dictionary defining the boundaries
    of the domain. This can then be accessed by higher
    level functions to create the visualization, using
    the specified domain.
    """

    domainInfo = {}
    domainInfo['xlim'] = xlim
    domainInfo['ylim'] = ylim
    domainInfo['zlim'] = zlim
    domainInfo['tlim'] = tlim

    return domainInfo
