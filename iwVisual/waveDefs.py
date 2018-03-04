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
    def plotwave(self, ax, i = 0):
    #    ax.clear()
    #    ax.plot(wave.domainGrid['xg'], wave1d(t[i]))
        ax.plot(self.xg, self.wave1d(self.tg[i]))

    # ------------------------------------
#    def moviewave(fig):
#        animation.FuncAnimation(fig,
#                                plotwave,
#                                frames = range(1, len(test_data)),
#                                interval = 1000, repeat = False)

    # ------------------------------------
    def moviewave(self, ax):
        for i in self.tg:
            ax.clear()
            plotwave(ax, i)
            plt.pause(0.1)
