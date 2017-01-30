import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid

sin1 = Sinusoid(Fs=1000, amp=5, freq=20, phase=5)
sin2 = Sinusoid(Fs=1000, amp=10, freq=40, phase=10)
sin3 = Sinusoid(Fs=1000, amp=15, freq=60, phase=15)
N = len(sin1.data)
print N
signal = []
for a in range(N):
    signal.append(sin1.data[a]+sin2.data[a]+sin3.data[a])
plt.plot(signal)
plt.show()

bin = 48
k = bin

cosa = []
sina = []

for n in range (N-1):
    theta = 2*math.pi*k*n/N
    cosa.append(math.cos(theta))
    sina.append(math.sin(theta))

plt.plot(abs(np.fft.fft(cosa)))
plt.show()
plt.plot(abs(np.fft.fft(sina)))
plt.show()

bin = 48.5
k = bin

cosa = []
sina = []

for n in range (N-1):
    theta = 2*math.pi*k*n/N
    cosa.append(math.cos(theta))
    sina.append(math.sin(theta))

plt.plot(abs(np.fft.fft(cosa)),'b.-')
plt.show()
plt.plot(abs(np.fft.fft(sina)),'b.-')
plt.show()