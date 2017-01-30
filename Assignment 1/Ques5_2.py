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
#phase goes random
phase = np.random.randn(length)
sigC = []
for n in range (length):
    val1 = magnitude[n]*math.cos(phase[n])
    val2 = magnitude[n]*math.sin(phase[n])
    sigC.append(np.complex(val1,val2))
#find inverse transform
waveifft = np.fft.ifft(sigC)
#write back the signal object
sig = Signal(data=waveifft)
sig.wav_write('Ques5_2Output.wav')