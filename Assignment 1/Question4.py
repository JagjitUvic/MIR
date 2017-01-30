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

signal = []
for a in range(N):
    signal.append(sin1.data[a]+sin2.data[a]+sin3.data[a])
plt.plot(abs(np.fft.fft(signal)))
plt.show()

sin4 = Sinusoid(Fs=1000, amp=5, freq=20, phase=5)

N = len(sin4.data)

bin = 60
k = bin

cosa = []
sina = []

for n in range (N):
    theta = 2*math.pi*k*n/N
    cosa.append(math.cos(theta))
    sina.append(math.sin(theta))

plt.plot(cosa)
plt.show()
plt.plot(sina)
plt.show()

ppc = []
pps = []
print len(signal)
print len(cosa)
for n in range(N):
    ppc.append(cosa[n] * signal[n])
    pps.append(sina[n] * signal[n])

print np.arctan(sum (pps)/sum(ppc))
plt.plot(ppc)
plt.show()
plt.plot(pps)
plt.show()