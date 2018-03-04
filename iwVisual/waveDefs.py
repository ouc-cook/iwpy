import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------
class PlaneWave1d:

    #
    a = 1
    phi0 = 0

    #
    k = np.nan
    wvfreq = np.nan

    #
    xg = np.nan
    tg = np.nan

    # ------------------------------------
    # Create array with n lines where n = len(t)
    def wave1d(self, t = tg):
        return self.a * np.cos(self.k * self.xg +
                               self.wvfreq * t +
                               self.phi0)

    # ------------------------------------
    def plotwave(i):
    #    ax.clear()
        ax.plot(wave.domainGrid['xg'], wave1d(t[i]))

    # ------------------------------------
    def moviewave(fig):
        animation.FuncAnimation(fig,
                                plotwave,
                                frames = range(1, len(test_data)),
                                interval = 1000, repeat = False)

    # ------------------------------------
    def planewave1d(wave):
        for i  in wave.domainGrid['tg']:
            plot(wave.domainGrid['xg'], wave.wave1d(i))
