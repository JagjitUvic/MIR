import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid
from mir import Signal

sin = Signal()

sin.wav_read('classical1.wav')
mel1 = sin.data

sin.wav_read('metal2.wav')
mel2 = sin.data


WS = 2048

list1 = []
cfreqs1 =[]
sin1 =[]
for n in range (0,len(mel1),WS):
    list_temp1 = mel1[n:n+WS]
    dft1 = np.fft.fft(list_temp1)
    magnitudes1 = np.abs(dft1)  # magnitudes
    freqs1 = 0
    den1 = 0
    for i in range(0, len(magnitudes1)/2):
        freqs1 += i * magnitudes1[i]
        den1 += magnitudes1[i]
    wave1 = Sinusoid(duration=len(magnitudes1) / 44100.0, freq=(freqs1 / den1)*21.5)
    cfreqs1.append((freqs1 / den1)*21.5)
    for j in range(0, len(wave1.data)):
        sin1.append(wave1.data[j])

list2 = []
cfreqs2 =[]
sin2 = []
for n in range (0,len(mel2),WS):
    list_temp2 = mel2[n:n+WS]
    dft2 = np.fft.fft(list_temp2)
    magnitudes2 = np.abs(dft2)  # magnitudes
    freqs2 = 0
    den2 = 0
    for i in range(0, len(magnitudes2)/2):
        freqs2 += i * magnitudes2[i]
        den2 += magnitudes2[i]
    wave2 = Sinusoid(duration=len(magnitudes2) / 44100.0, freq=(freqs2 / den2)*21.5)
    cfreqs2.append((freqs2 / den2)*21.5)
    for j in range(0, len(wave2.data)):
        sin2.append(wave2.data[j])


plt.plot(cfreqs2)
plt.plot(cfreqs1)
plt.show()
