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
waveifft = np.fft.ifft(wavefft)
#Writing the audio file
sig = Signal(data=waveifft)
sig.wav_write('Ques5Output.wav')