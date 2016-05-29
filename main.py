import pickle
import cv2 as cv
import numpy as np
import multiprocessing as mp
from utils import signal as us
from utils import shapes as yo
from utils import amplitudes as ua
from matplotlib import pyplot as plt

def norm(this):
    """ Squeeze to 0-1 """
    this -= this.min()
    this /= this.max()
    return this

def funky_image(XX, YY, tick):
    """ Generate some funk """
    with open('xf_yo.pickle') as fin:
        notes = pickle.load(fin)

    lo, mi, hi = ua.notes2amps(notes)
    full = lo + mi + hi
    # This sums to circa 333
    full = np.cumsum(full)
    rlo = np.cumsum(lo)

    # phi = 4*np.pi * 2 * tick/4000.0
    phi = 4*np.pi * full[tick]/400.0
    the = 2*np.pi * 2 * tick/1250.0
    the = 4*np.pi * rlo[tick]/rlo[-1]

    r_shift = 16 + 3 * np.cos(the)

    a_hahn = yo.Hahn(k = 0.5, r = 5, m = 10)

    # Some factors
    freqs = [0.5  for it in range(20)]
    lmbds = [5 for it in range(20)]

    # Partial drawings container
    frames = []

    howmany = 8
    for it in range(howmany):
        phi += 2.0 * np.pi/howmany
        ax_shift = r_shift * np.cos(phi)
        ay_shift = r_shift * np.sin(phi)

        # This seem to be adding a nice twist
        # if it == 8:
        #     a_hahn._k = 2

        a_hahn.set_x_shift(ax_shift)
        a_hahn.set_y_shift(ay_shift)
        frames.append(a_hahn.get(XX, YY, tick))

    Z = np.zeros_like(frames[0])

    for frame in frames:
        Z += frame

    # le normalizatione
    Z -= Z.min()
    Z /= Z.max()
    Z *= 140 + 32* np.cos(phi**2) * np.sin(the/3.) ** 2 + 40 *lo[tick]

    # OpenCV likes uint8
    return np.uint8(Z)

def make_single(tick):
    """ Parallel ready single image generator """
    print tick
    if False:
        x_res = 1920
        y_res = 1080
    else:
        x_res = 490
        y_res = 380

    xspan = 4.5 - 2*np.cos(2.0 * np.pi * tick/100)
    yspan = 4.5 - 2*np.cos(2.0 * np.pi * tick/100)
    x = np.linspace(-xspan, xspan, x_res)
    y = np.linspace(-yspan, yspan, y_res)
    XX, YY = np.meshgrid(x, y)

    ZZ = funky_image(XX, YY, tick)
    filename = 'imgs/{}.png'.format(int(1e7 + tick))
    img = cv.applyColorMap(ZZ, cv.COLORMAP_JET)
    cv.imwrite(filename, img)

def main():
    """ blurp """
    # blompf notes sample PITCH | START | DURATION | VOLUME
    notes = [[45, 0, 8, 70],
             [48, 0, 8, 69],
             [53, 0, 8, 69],
             [35, 0, 8, 72],
             [43, 8, 16, 69],
             [50, 8, 16, 68],
             [53, 8, 16, 68]]

    amps = ua.notes2amps(notes)

    tick_range = range(200)
    pool = mp.Pool(processes = mp.cpu_count())
    pool.map(make_single, tick_range)

if __name__ == '__main__':
    main()
