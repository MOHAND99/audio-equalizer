import tkinter as tk
import scipy.io.wavfile as wav
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
