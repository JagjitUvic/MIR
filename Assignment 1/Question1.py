import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid

sin = Sinusoid(Fs=100)
datar = sin.data.real
datai = sin.data.imag
N = len(datar)
outputr = []
outputi = []
for k in range(N):
    sumr = 0
    sumi = 0
    for n in range(N):
        sumr += datar[n]*math.cos(2*math.pi*k*n/N)+datai[n]*math.sin(2*math.pi*k*n/N)
        sumi += -datar[n]*math.sin(2*math.pi*k*n/N)+datai[n]*math.cos(2*math.pi*k*n/N)
    outputr.append(sumr)
    outputi.append(sumi)
outputp = []

for a in range(N):
    outputp.append(math.sqrt((outputr[a]*outputr[a])+(outputi[a]*outputi[a])))

plt.plot(outputp)
plt.show()

outputk = sin.dft()
plt.plot(abs(outputk))
plt.show()
