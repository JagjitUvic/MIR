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

part1 = np.fft.fft(mel1)
partc1 = np.conj(part1)*part1
parta1 = np.fft.ifft(partc1)

for n in range (0,len(mel1),WS):
    list_temp1 = parta1[n:n+WS]
    dft1 = np.fft.fft(list_temp1)
    peak1 = np.argmax(dft1[0:len(dft1)/2])
    freq1 = peak1*21.5
    list1.append(freq1)

list1a = []

for n in range (0,len(mel1),WS):
    list_temp1 = mel1[n:n+WS]
    dft1 = np.fft.fft(list_temp1)
    peak1 = np.argmax(dft1[0:len(dft1)/2])
    freq1 = peak1*21.5
    list1a.append(freq1)

list1f =[]

for m in range (len(list1)):
    list1f.append(list1[m]+list1a[m])

plt.plot(list1f)
plt.show()



list2 = []

part2 = np.fft.fft(mel2)
partc2 = np.conj(part2) * part2
parta2 = np.fft.ifft(partc2)

for n in range (0,len(parta2),WS):
    list_temp2 = parta2[n:n+WS]
    dft2 = np.fft.fft(list_temp2)
    peak2 = np.argmax(dft2[0:len(dft2)/2])
    freq2 = peak2*21.5
    list2.append(freq2)

list2a =[]

for n in range (0,len(mel2),WS):
    list_temp2 = mel2[n:n+WS]
    dft2 = np.fft.fft(list_temp2)
    peak2 = np.argmax(dft2[0:len(dft2)/2])
    freq2 = peak2*21.5
    list2a.append(freq2)

list2f =[]
for m in range (len(list2)):
    list2f.append(list2[m]+list2a[m])

plt.plot(list2f)
plt.show()

list3 = []
part3 = np.fft.fft(mel3)
partc3 = np.conj(part3) * part3
parta3 = np.fft.ifft(partc3)

for n in range (0,len(parta3),WS):

    list_temp3 = parta3[n:n+WS]
    dft3 = np.fft.fft(list_temp3)
    peak3 = np.argmax(dft3[0:len(dft3)/2])
    freq3 = peak3*21.5
    list3.append(freq3)

list3a =[]

for n in range (len(mel3),WS):
    list_temp3 = mel3[n:n+WS]
    dft3 = np.fft.fft(list_temp3)
    peak3 = np.argmax(dft3[0:len(dft3)/2])
    freq3 = peak3*21.5
    list3a.append(freq3)

list3f =[]
for m in range (len(list3a)):
    list3f.append(list3[m]+list3a[m])

plt.plot(list3f)
plt.show()