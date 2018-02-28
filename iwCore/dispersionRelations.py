# Functions
#
# Olavo Badaro Marques

#__all__ = []

import numpy as np
import matplotlib.pyplot as plt
#import

# ------------------------------------

# ------------------------------------
def iwChar(wvfreq, f0, N):
    """ Compute the internal wave characteristic
    angle with the horizontal.

    """

    rayChar = np.sqrt( (wvfreq**2 - f0**2) / (N**2 - wvfreq**2) )

    return rayChar


# ------------------------------------
def m2k(m, wvfreq, f0, N):
    """ Compute the horizontal wavenumber from
    the vertical wavenumber and the dispersion
    relationship.

    """

    k = m / iwChar(wvfreq, f0, N)

    return k
