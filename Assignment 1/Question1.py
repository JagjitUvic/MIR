import numpy as np
import matplotlib.pyplot as plt
import math
import mir
from mir import Sinusoid
#get the sin wave
sin = Sinusoid(Fs=100)
#differentiate real and imaginary components
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
#final output
for a in range(N):
    outputp.append(math.sqrt((outputr[a]*outputr[a])+(outputi[a]*outputi[a])))
#plot output
plt.plot(outputp)
plt.show()
#find the plot dft with built in function
outputk = sin.dft()
plt.plot(abs(outputk))
plt.show()
