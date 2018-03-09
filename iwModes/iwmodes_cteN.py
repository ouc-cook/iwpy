# Functions to make calculations for
# individual standard oceanic vertical modes.
#
# Olavo Badaro Marques

import numpy as np
import matplotlib.pyplot as plt
# need to import other internal wave files!!!

# ----------------------------------------
def horizwvlen(wvfreq, N, f0, D, nmd):

    m = nmd * np.pi / D
    k = m2k(m, wvfreq, f0, N)

    l = 2 * np.pi / k
    return l

# ----------------------------------------
def cn2cp(cn, wvfreq, lat):
    factor = wvfreq / (sqrt(wvfreq**2 - f0**2))
    cp = cn * times_factor
    return cp

# ----------------------------------------
def cn2cg(cn, wvfreq, lat):
    factor = wvfreq / (sqrt(wvfreq**2 - f0**2))
    cg = cn / factor
    return cg
