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

for n in range (0,len(mel1),WS):
    list_temp1 = mel1[n:n+WS]
    dft1 = np.fft.fft(list_temp1)
    peak1 = np.argmax(dft1[0:len(dft1)/2])
    freq1 = peak1*21.5
    list1.append(freq1)

plt.plot(list1)
plt.show()

list2 = []
for n in range (0,len(mel2),WS):
    list_temp2 = mel2[n:n+WS]
    dft2 = np.fft.fft(list_temp2)
    peak2 = np.argmax(dft2[0:len(dft2)/2])
    freq2 = peak2*21.5
    list2.append(freq2)

plt.plot(list2)
plt.show()

list3 = []
for n in range (0,len(mel3),WS):
    list_temp3 = mel3[n:n+WS]
    dft3 = np.fft.fft(list_temp3)
    peak3 = np.argmax(dft3[0:len(dft3)/2])
    freq3 = peak3*21.5
    list3.append(freq3)

plt.plot(list3)
plt.show()

