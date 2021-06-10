import numpy as np
from scipy import signal
from .pzmap import pzmap

freqs = np.array([[0, 170],
                  [170, 310],
                  [310, 600],
                  [600, 1000],
                  [1000, 3000],
                  [3000, 6000],
                  [6000, 12000],
                  [12000, 14000],
                  [14000, 16000]])


def plot_zeros_poles(p_z):
    for ele in (p_z):
        z = signal.TransferFunction(ele[0], ele[1])
        pzmap(z.zeros, z.poles)
