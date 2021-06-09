import scipy.signal
from helper_method import freqs


def design_fir_system(fs=1600, order=101, freqs=freqs):

    filters = [[]] * len(freqs)
    filters[0] = scipy.signal.firwin(order,
                                     freqs[0][1]/fs,
                                     window="hamming")

    for i in range(1, len(freqs)):
        filters[i] = scipy.signal.firwin(order,
                                         freqs[i] / fs,
                                         window="hamming",
                                         fs=fs)

    return filters


print(design_fir_system())
