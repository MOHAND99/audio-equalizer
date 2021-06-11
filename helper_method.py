import numpy as np
from pzmap import pzmap
from scipy import signal
import matplotlib.pyplot as plt


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

    filters = []

    freqs[0] = freqs[0] / fs
    if freqs[0][1] < 1:
        filters.append([signal.firwin(order + 1, freqs[0][1])])

    for i in range(1, len(freqs)):
        freqs[i] = freqs[i] / fs
        if freqs[i][1] < 1:
            filters.append(signal.firwin(order + 1, freqs[i]))
            continue
        break

    return filters


def iir_filter(order, fs):
    iir_filters = []
    bands = get_bands()
    for i in range(len(bands)):
        lis = [bands[i][0] * 2 / fs, bands[i][1] * 2 / fs]
        if lis[1] >= 1:
            return iir_filters
        if lis[0] == 0:
            current_filter = signal.iirfilter(
                                            order, lis[1],
                                            output='zpk',
                                            btype='lowpass')
        else:
            current_filter = signal.iirfilter(order, lis, output='zpk')
        iir_filters.append([current_filter])

    return iir_filters


def plot_zeros_poles(poles_zeros):
    for ele in poles_zeros:
        pzmap(ele[0][0], ele[0][1])


def plot_mag_phase(filters, fs):
    for fi in filters:
        w, h = signal.freqz_zpk(fi[0][0], fi[0][1], fi[0][2], fs=fs)
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_title('Digital filter frequency response')
        ax1.plot(w, 20 * np.log10(abs(h)), 'b')
        ax1.set_ylabel('Amplitude [dB]', color='b')
        ax1.set_xlabel('Frequency [Hz]')
        ax1.grid()
        ax2 = ax1.twinx()
        angles = np.unwrap(np.angle(h))
        ax2.plot(w, angles, 'g')
        ax2.set_ylabel('Angle [radians]', color='g')
        plt.axis('tight')
    plt.show()


def plot_impl_unitstep(filters):
    for filter in filters:
        impulse = np.repeat(0., 60)
        impulse[0] = 1.
        x = np.arange(0, 60)
        coff = signal.ZerosPolesGain(filter[0][0], filter[0][1], filter[0][2])
        # Compute the impulse response
        response = signal.lfilter(coff.to_tf().num, coff.to_tf().den, impulse)
        # Plot filter impulse and step response:
        fig = plt.figure(figsize=(10, 6))
        plt.subplot(211)
        plt.stem(x, response, 'm', use_line_collection=True)
        plt.ylabel('Amplitude', fontsize=15)
        plt.xlabel(r'n (samples)', fontsize=15)
        plt.title(r'Impulse response', fontsize=15)
        plt.subplot(212)
        step = np.cumsum(response)
        # Compute step response of the system
        plt.stem(x, step, 'g', use_line_collection=True)
        plt.ylabel('Amplitude', fontsize=15)
        plt.xlabel(r'n (samples)', fontsize=15)
        plt.title(r'Step response', fontsize=15)
        plt.subplots_adjust(hspace=0.5)
        fig.tight_layout()
    plt.show()
