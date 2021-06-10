import tkinter as tk
import soundfile as sf
import numpy as np
from helper_method import get_bands, iir_filter
from tkinter import filedialog
from scipy import signal

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
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

order = 100
if filter_type == 'iir':
    # Figure out if we want to use fs from user input here..
    filters = iir_filter(order, fs)
elif filter_type == 'fir':
    pass

output = np.zeros_like(data)
for filter in filters:
    output = output + signal.lfilter(filter[0][0], filter[0][1], data)
