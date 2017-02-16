import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid
from mir import Signal

sig = Signal()
#Read audio File
sig.wav_read('Ques5Input.wav')
wave = sig.data
wavefft = np.fft.fft(wave)
length = len(wavefft)
magnitude = []
phase = []
for n in range (length):
    magnitude.append(np.absolute(wavefft[n]))
    phase.append(np.angle(wavefft[n]))
#fetching 4 high values of magnitude
index = []
value = []
for n in range (4):
    index.append(np.argmax(magnitude))
    value.append(np.amax(magnitude))
    magnitude[np.argmax(magnitude)] = 0
#setting 4 high values rest all 0 if you use this logic it will be get same
use a for loop to check this

for n in range (length):
    if n == index[0]:
        magnitude[n] = value[0]
    elif n == index[1]:
        magnitude[n] = value[1]
    elif n == index[2]:
        magnitude[n] = value[2]
    elif n == index[3]:
        magnitude[n] = value[3]
    else:
        magnitude[n] = 0
sigC = []
for n in range (length):
    val1 = magnitude[n]*math.cos(phase[n])
    val2 = magnitude[n]*math.sin(phase[n])
    sigC.append(np.complex(val1,val2))
#find inverse transform
waveifft = np.fft.ifft(sigC)
#write back the signal object
sig = Signal(data=waveifft)
sig.wav_write('Ques5_3Output.wav')