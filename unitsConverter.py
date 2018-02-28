# Functions to convert
#
# Olavo Badaro Marques

#__all__ = []

# ------------------------------------

def convFactor:
    return (2*pi/(24*3600))

def cpd2rps(freq):

    return freq*convFactor()

def rps2cpd(freq):

    return freq/convFactor()
