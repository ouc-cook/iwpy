import numpy as np
#import pandas as pd

def wavedomain(xlim, ylim = np.NaN, zlim = np.NaN, tlim = np.NaN):
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
