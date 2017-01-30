import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid

sin1 = Sinusoid(Fs=256, amp=5, freq=20, phase=5)

N = len(sin1.data)
print N
signal = []

bin = 4
k = bin

cosa = []
sina = []

for n in range (N-1):
    theta = 2*math.pi*k*n/N
    cosa.append(math.cos(theta))
    sina.append(math.sin(theta))

plt.plot(cosa)
plt.show()
plt.plot(sina)
plt.show()
