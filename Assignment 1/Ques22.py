import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid
from mir import Signal

sin = Signal()
sin.wav_read('2.wav')
wave = sin.data
wave = wave[0:2048]

hann = np.hanning(2048)
wave1 =[]
N = 2048
for n in range (N):
    wave1.append(hann[n]*wave[n])

dft = np.fft.fft(wave1)
dftt= abs(dft)
plt.plot(20*np.log10(dftt))
plt.show()