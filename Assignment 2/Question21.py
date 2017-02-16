import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid
from mir import Signal

sin = Signal()

sin.wav_read('melody.wav')
mel1 = sin.data

sin.wav_read('melody1.wav')
mel2 = sin.data

sin.wav_read('melody2.wav')
mel3 = sin.data

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

sig1= Signal(data = sin1)
#output new audio file
sig1.wav_write('mel1sys.wav',normalize=True)

plt.plot(cfreqs1)
plt.show()

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

sig2 = Signal(data=sin2)
# output new audio file
sig2.wav_write('mel2sys.wav', normalize=True)

plt.plot(cfreqs2)
plt.show()


list3 = []
cfreqs3 =[]
sin3 =[]
for n in range (0,len(mel3),WS):
    list_temp3 = mel3[n:n+WS]
    dft3 = np.fft.fft(list_temp3)
    magnitudes3 = np.abs(dft3)  # magnitudes
    freqs3 = 0
    den3 = 0
    for i in range(0, len(magnitudes3)/2):
        freqs3 += i * magnitudes3[i]
        den3 += magnitudes3[i]
    wave3 = Sinusoid(duration=len(magnitudes3) / 44100.0, freq=(freqs3 / den3)*21.5)
    cfreqs3.append((freqs3 / den3)*21.5)
    for j in range(0, len(wave3.data)):
        sin3.append(wave3.data[j])

sig3 = Signal(data=sin3)
# output new audio file
sig3.wav_write('mel3sys.wav', normalize=True)

plt.plot(cfreqs3)
plt.show()