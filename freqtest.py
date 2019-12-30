# -*- coding: utf-8 -*-

import pyaudio
import numpy as np
from random import randrange


def sine(frequency, duration):
    p = pyaudio.PyAudio()
    
    volume = 1       # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    
    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*frequency/fs)).astype(np.float32)
    
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    
    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples)
    
    stream.stop_stream()
    stream.close()
    
    p.terminate()
    
dichoMode = True

N = 12
minFreq = 13000
maxFreq = 22000
for i in range(N):
    
    if dichoMode:
        freq = (minFreq + maxFreq) / 2
    else:
        freq = randrange(minFreq, maxFreq)
    sine(freq, 3)
    ask = True
    while ask:
        ans = input("Heard? (y/n)")
        if ans == 'y':
            minFreq = freq
            ask = False
        elif ans == 'n':
            maxFreq = freq
            ask = False
        else:
            print("Wrong input")

print("Minimum heard: " + str(minFreq))
print("Maximum heard: " + str(maxFreq))