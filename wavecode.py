import numpy as np
from math import pi
from math import fmod
from random import random
from scipy.integrate import quad
depths = np.array([0,1,1,1,1,0])
refraction = np.array([1,1.5,2.5,1.5,2.5,1])
length = refraction.size


def reflection(n1, n2):
    return ((n1-n2)/(n1+n2))**2

wavelength = 4
omega = 2 * pi / wavelength

phase = np.zeros(samples)
exit = np.ones(samples, dtype="bool_")
for i in range(samples):
    index = 0
    direction = 1
    while not ((index == 1 and direction == -1) or (index == length-1 and direction == 1)):
        #print(index, direction)
        depth = depths[index] if direction == 1 else depths[index-1]
        phase[i]+= depth * omega
        index+=direction
        prob = reflection(refraction[index-direction], refraction[index])
        if random() > prob:
            direction*=-1
            phase[i]+=pi
        continue
    if index == length-1:
        exit[i]=False
    
phase = phase[exit]
print(quad(lambda x: np.square(np.sum(np.sin(phase+x))/samples)/pi, 0, 2*pi))
print("Escaped samples:",samples-np.sum(exit))