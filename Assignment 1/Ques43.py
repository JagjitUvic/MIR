import numpy as np
import matplotlib.pyplot as plt
import math
import mir
from mir import Sinusoid
from mir import Signal
from mir import Mixture

#midi notes from 0-119
note = [7,8,9,10]
freq = []
list = []
for n in range (4):
    freq.append(440*pow((note[n]-57)/12,2))
    sin = Sinusoid(freq=freq[n])
    list.append(sin)

#make signal mixture
mix1 = Mixture(*list)

sig1 = Signal(data=mix1.data)
#output new audio file
sig1.wav_write('melody.wav',normalize=False)

mix1.plot()
