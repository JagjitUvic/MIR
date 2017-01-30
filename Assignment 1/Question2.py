import numpy as np
import matplotlib.pyplot as plt
import math
import mir
from mir import Sinusoid
#fetch the 3 sinusoids
sin1 = Sinusoid(Fs=1000, amp=5, freq=20, phase=5)
sin2 = Sinusoid(Fs=1000, amp=10, freq=40, phase=10)
sin3 = Sinusoid(Fs=1000, amp=15, freq=80, phase=15)
N = len(sin1.data)
signal = []
#Make them one
for a in range(N):
    signal.append(sin1.data[a]+sin2.data[a]+sin3.data[a])
plt.plot(signal)
plt.show()
#calculating for bin 48
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
#calculating between bins
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