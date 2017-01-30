import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid

N = 2048

bin = 525
k = bin

sina = []

for n in range (N):
    theta = 2*math.pi*k*n/N
    sina.append(math.sin(theta))

N = 2048

bin = 600.5
k = bin

sinaa = []

for n in range (N):
    theta = 2*math.pi*k*n/N
    sinaa.append(math.sin(theta))

N = 2048

bin = 525.5
k = bin

sinaaa = []

for n in range (N):
    theta = 2*math.pi*k*n/N
    sinaaa.append(math.sin(theta))

hann = np.hanning(2048)
wave =[]
for n in range (N):
    wave.append(hann[n]*sinaaa[n])

dft3 = np.fft.fft(wave)
dft2 = np.fft.fft(sinaa)
dft = np.fft.fft(sina)
dft3t= abs(dft3)
dft2t= abs(dft2)
dftt= abs(dft)
plt.plot(20*np.log10(dft3t))
plt.plot(20*np.log10(dft2t))
plt.plot(20*np.log10(dftt))
plt.show()