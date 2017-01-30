import numpy as np
import matplotlib.pyplot as plt
import math
import mir
from mir import Sinusoid
from mir import Signal
from mir import Mixture

#Frequency and Amplitude for Sound 1
freq = [292,563,869,1160,1439,1767,2064,2828,3159,3447]
amp = [0.15488166189124816,0.03162277660168379,0.019275249131909367,0.008511380382023767,0.0023173946499684774,0.0007328245331389037,0.0007673614893618193,0.0003388441561392024,0.00031988951096913973,0.00030549211132155157]

list = []
for n in range (10):
    sin = Sinusoid(amp=amp[n], freq=freq[n])
    list.append(sin)
#make signal mixture
mix1 = Mixture(*list)

sig1 = Signal(data=mix1.data)
#output new audio file
sig1.wav_write('flu_new.wav',normalize=False)

mix1.plot()
#Frequency and Amplitude for Sound 2
freq = [295,572,882,1165,1460,1764,2052,2343,2633,2931]
amp = [0.0812830516164099,0.06165950018614822,0.06095368972401691,0.07852356346100718,0.03890451449942807,0.042169650342858224
    ,0.033884415613920256,0.006760829753919818,0.022130947096056376,0.01428893958511103]

list1 = []
for n in range (10):
    sin = Sinusoid(amp=amp[n], freq=freq[n])
    list1.append(sin)
#make signal mixture
mix2 = Mixture(*list1)

sig2 = Signal(data=mix2.data)
#output new audio file
sig2.wav_write('voi_new.wav',normalize=False)

mix2.plot()