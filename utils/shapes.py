"""
    Set of functions that may be used as basic 2D shapes for
    cymatic constructions from the blompf project note-sets
"""

import numpy as np

class Hahn(object):
    """
    Otto Hahn was a German chemist and pioneer in the fields
    of radioactivity and radiochemistry who won the Nobel Prize
    in Chemistry in 1944 for the discovery and the radiochemical
    proof of nuclear fission.
    """
    def __init__(self, m = 2, n = 2, k = 13., r = 80.):
        """ el Creador """
        self._m = m
        self._n = n
        self._k = k
        self._r = r

    def get(self, x, y, tick):
        """ Gets the shape at time tick """
        # Simplify notation
        mm = self._m
        nn = self._n
        kk = self._k
        rr = self._r
        out = np.sin(kk * (x**mm + y**nn) + tick/rr)
        # out = np.sin(kk * (x**mm + y**nn) + np.sin(tick/rr))
        return out

class Fritz(object):
    """
    Friedrich Wilhelm "Fritz" Strassmann was a German chemist
    who, with Otto Hahn in 1938, identified barium in the
    residue after bombarding uranium with neutrons, results
    which, when confirmed, demonstrated the previously unknown
    phenomenon of nuclear fission.
    """
    def __init__(self, m = 2, n = 2):
        """ el Konsdrukdor """
        self._m = m
        self._n = n

    def get(self, x, y, tick):
        """ Get it """
        # Simplify notation
        mm = self._m
        nn = self._n
        out = np.cos(tick/30. + 3 * np.arctan2(x**mm, y**nn))
        return out

class Meitner(object):
    """
    Lise Meitner was an Austrian physicist who worked on
    radioactivity and nuclear physics. Otto Hahn and Meitner
    led the small group of scientists who first discovered
    nuclear fission of uranium when it absorbed an extra neutron;
    the results were published in early 1939.
    """
    def __init__(self, m = 2, n = 2):
        """ el Konsdrukdor """
        self._m = m
        self._n = n

    def get(self, x, y, tick):
        # Simplify notation
        mm = self._m
        nn = self._n
        out = np.cos(tick/nn + mm * np.arctan2(x, y))
        return out