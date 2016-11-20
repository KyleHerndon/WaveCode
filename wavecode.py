depths = [1,1,1,1]
indexOfRefraction = [1.5,2.5,1.5,2.5]

samples = 100

def reflection(n1, n2):
    return ((n1-n2)/(n1+n2))**2

class Wave:
    def __init__(self, amplitude, phase):
        self.amplitude = amplitude
        self.phase = phase

