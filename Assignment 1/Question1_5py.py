import numpy as np
import matplotlib.pyplot as plt
import math
import mir
from mir import Sinusoid
import time
start_time = time.time()
size = [256,512,1024,2048]

for n1 in range(4):
    for n2 in range(100):
        #get the sin wave
        sin = Sinusoid(Fs=size[n1])
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
    print("Time for N --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
size = [256,512,1024,2048]
output = []
for n1 in range(4):
    for n2 in range(100):
        #get the sin wave
        sin = Sinusoid(Fs=size[n1])
        output = sin.dft()
    print("Time for N --- %s seconds ---" % (time.time() - start_time))

