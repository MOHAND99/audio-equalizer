import numpy as np
from pzmap import pzmap
import scipy.signal


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


def design_fir_system(fs, order=100, freqs=get_bands()):

    filters = [[]] * len(freqs)

    freqs[0] = freqs[0] / fs
    if freqs[0][0] > 0 and freqs[0][1] < 1:
        filters[0] = scipy.signal.firwin(order + 1,
                                         freqs[0][1]/fs,
                                         window="hamming")

    for i in range(1, len(freqs)):
        freqs[i] = freqs[i] / fs
        if freqs[i][0] > 0 and freqs[i][1] < 1:
            filters[i] = scipy.signal.firwin(order + 1,
                                             freqs[i],
                                             window="hamming",
                                             fs=fs)

    return filters


def iir_filter(order, fs):
    iir_filters = []
    bands = get_bands()
    for i in range(len(bands)):
        lis = [bands[i][0] / fs, bands[i][1] / fs]
        if lis[1] >= 1:
            return iir_filters
        if lis[0] == 0:
            current_filter = scipy.signal.iirfilter(order,
                                                    lis[1], btype='lowpass')
        else:
            current_filter = scipy.signal.iirfilter(order, lis)
        iir_filters.append([current_filter])

    return iir_filters


def plot_zeros_poles(p_z):
    for ele in (p_z):
        z = scipy.signal.TransferFunction(ele[0], ele[1])
        pzmap(z.zeros, z.poles)
