import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------
def wave1d(t):
    # Create array with n lines where n = len(t)
    wave1datt = a * cos(k * wave.domainGrid['xg'] + wvfreq * t + phi0)

# ------------------------------------
def planewave1d(wave):
    for i in wave.domainGrid['tg']:
        plot(wave.domainGrid['xg'], wave.wave1d(i))
