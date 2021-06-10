import numpy as np
from scipy import signal
from pzmap import pzmap


def get_bands():
    return np.array([[0, 170],
                     [170, 310],
                     [310, 600],
                     [600, 1000],
                     [1000, 3000],
                     [3000, 6000],
                     [6000, 12000],
                     [12000, 14000],
                     [14000, 16000]])


def iir_filter(order, fs):
    iir_filters = []
    bands = get_bands()
    for i in range(len(bands)):
        lis = [bands[i][0] / fs, bands[i][1] / fs]
        if lis[1] >= 1:
            return iir_filters
        if lis[0] == 0:
            current_filter = signal.iirfilter(order, lis[1], btype='lowpass')
        else:
            current_filter = signal.iirfilter(order, lis)
        iir_filters.append([current_filter])

    return iir_filters


def plot_zeros_poles(p_z):
    for ele in (p_z):
        z = signal.TransferFunction(ele[0], ele[1])
        pzmap(z.zeros, z.poles)
