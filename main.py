import tkinter as tk
import soundfile as sf
import numpy as np
from helper_method import (get_bands, plot_mag_phase,
                           iir_filters, fir_filters,
                           plot_impl_unitstep, plot_zeros_poles)
from scipy import signal

root = tk.Tk()
root.withdraw()
filetypes = [("wav files", ".wav")]
file_path = tk.filedialog.askopenfilename(title="Select .wav file",
                                          filetypes=filetypes)
data, fs = sf.read(file_path)
data = np.asarray(data)
print("File information:")
print(f"Path: {file_path}")
print(f"Data dimensions: {np.shape(data)}")
print(f"Frequency: {fs}")

bands = get_bands()
gains = []
for band in bands:
    gain = int(input(f"Enter the gain (in dB) for band {band}: "))
    gains.append(gain)

filter_type = input("Enter filter type (iir or fir): ")
output_fs = int(input("Enter the output sample rate: "))

filters = None
if filter_type == 'iir':
    filters = iir_filters(2, output_fs)
elif filter_type == 'fir':
    filters = fir_filters(4, output_fs)

# plot_zeros_poles(filters)
plot_mag_phase(filters, output_fs)
# plot_impl_unitstep(filters)
output = np.zeros_like(data)
for i, filter in enumerate(filters):
    current = signal.lfilter(filter[0], filter[1], data)
    # TODO: Draw current in time and frequency domain
    output = output + current * (10 ** (gains[i] / 20))
# TODO: Draw output in time and frequency domain

output_file_name = tk.filedialog.asksaveasfilename(title="Save wav file",
                                                   defaultextension='.wav',
                                                   filetypes=filetypes)
sf.write(output_file_name, output, output_fs)
input("Press any key to exit...")
