import numpy as np
import scipy.signal

freqs = np.array([[0, 170],
                  [170, 310],
                  [310, 600],
                  [600, 1000],
                  [1000, 3000],
                  [3000, 6000],
                  [6000, 12000],
                  [12000, 14000],
                  [14000, 16000]])


def design_fir_system(fs, order=100, freqs=freqs):

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
