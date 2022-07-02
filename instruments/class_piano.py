import numpy as np
import matplotlib.pyplot as plt

class Instrument(object):
    def __init__(self, filename, amplitud=[], envolvente={}):
        with open(filename, 'r') as f:
            print(len(filename))
            num_armonics = f.readline()
            for armonic in range(int(num_armonics)):
                line = f.readline().split(" ")
                amplitud.append(float(line[1]))
            for cosa in range(3): # 3 = len(filename) - num_armonics - 1
                line = f.readline().split(" ")
                envolvente[line[0]] = line[1]
                
        f.close()
        self.amplitud = amplitud
        self.envolvente = envolvente
        
    def notes(self):
        pass
                
 
class Piano(Instrument):
    def __init__(self, filename):
        Instrument.__init__(self, filename)


#piano = Piano("piano.txt")
                
                