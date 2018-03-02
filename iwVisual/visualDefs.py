import numpy as np
#import pandas as pd

def wavedomain(xlim, ylim, zlim = np.NaN, tlim = np.NaN):
    """ 
    """

    domainInfo = {}
    domainInfo['xlim'] = xlim
    domainInfo['ylim'] = ylim
    domainInfo['zlim'] = zlim
    domainInfo['tlim'] = tlim

    return domainInfo
