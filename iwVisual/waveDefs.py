import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------
class Wave1d:

    #
    a = 1
    k = 1
    wvfreq = 1
    phi0 = 1

    #
    xg = 1
    tg = 1

    # ------------------------------------
    def wave1d(self, t = tg):
        # Create array with n lines where n = len(t)
        return self.a * np.cos(self.k * self.xg +
                               self.wvfreq * t +
                               self.phi0)

# ------------------------------------
def plotwave1d(i):
#    ax.clear()
    ax.plot(wave.domainGrid['xg'], wave1d(t[i]))

# ------------------------------------
def planewave1d(fig):
    animation.FuncAnimation(fig,
                            plotwave1d,
                            frames = range(1, len(test_data)),
                            interval = 1000, repeat = False)

# ------------------------------------
def planewave1d(wave):
    for i  in wave.domainGrid['tg']:
        plot(wave.domainGrid['xg'], wave.wave1d(i))
