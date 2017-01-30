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
plt.plot(dftt)
plt.show()

dft1 = np.fft.fft(wave)
dft1t= abs(dft1)
plt.plot(dft1t)
plt.show()

wave = wave[0:256]
hann = np.hanning(256)
wave1 =[]
N = 256
for n in range (N):
    wave1.append(hann[n]*wave[n])

dft = np.fft.fft(wave1)
dftt= abs(dft)
plt.plot(dftt)
plt.show()

dft1 = np.fft.fft(wave)
dft1t= abs(dft1)
plt.plot(dft1t)
plt.show()

list = []
N = 2048
for n in range (N):
    if n < 255:
        list.append(wave[n])
    else:
        list.append('0')

dft1 = np.fft.fft(list)
dft1t= abs(dft1)
plt.plot(dft1t)
plt.show()

hann = np.hanning(2048)
wave1 = [x*y for x,y in zip([hann],list)]




dft = np.fft.fft(wave1)
dftt= abs(dft)
plt.plot(dftt)
plt.show()