import numpy as np
import matplotlib.pyplot as plt
import math
import mir
from mir import Sinusoid
from mir import Signal
from mir import Mixture

#Declare the frequency and amplitude array
freq = [100,200,300,400,500]
amp = [10,20,30,40,50]
#Declare the empty list
list = []
#Making a list of all 5 sinusoids
for n in range (5):
    sin = Sinusoid(amp=amp[n], freq=freq[n])
    list.append(sin)
#Making a mixture using the helper function in mir.py
mix = Mixture(*list)
#Plot the mixture of all 5 waves
mix.plot()