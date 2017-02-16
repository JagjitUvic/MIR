import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
import mir
from mir import Sinusoid
from mir import Signal

sin = Signal()
#Read audio File
sin.wav_read('Ques5Input.wav')
wave = sin.data
wavefft = np.fft.fft(wave)
length = len(wavefft)
print length
window =  length/32768
list = []
print window
#overlapping window
list.append(wavefft[0:32769])
list.append(wavefft[32768:65537])
list.append(wavefft[65536:131073])
list.append(wavefft[131072:262145])
#inverse and save back
waveifft = np.fft.ifft(list)
#write back the signal object
sig = Signal(data=waveifft)
sig.wav_write('Ques5_4Output.wav')