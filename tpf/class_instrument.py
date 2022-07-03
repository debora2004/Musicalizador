import notes
import math
import matplotlib as plt
import numpy as np


notes = notes.notes_mapping 

class Instrument:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            num_harmonics = f.readline().strip()
            self.harm_list = {}
            self.amp_mod = {} #modulador de amplitud
            
            # crea un diccionario donde las claves son el numero de armonico y la key es el multiplo e intensidad
            for n in range(int(num_harmonics)):
                mult_harm = f.readline()
                mult_harm = mult_harm.split(' ')
                self.harm_list[mult_harm[0]] = mult_harm[1].strip('\n')
                
            # crea un diccionario donde el primer elemento es attack, el segundo es sustain y el tercero es decay
            for amp in range(3):    # 3 = len(filename) - num_armonics - 1
                line = f.readline().split(" ")
                name_funct = line[0].strip()
                if len(line) == 4:
                    self.amp_mod[name_funct] =[line[1].strip(), line[2].strip(), line[3].strip()]
                elif len(line) == 3:
                    self.amp_mod[name_funct] = [line[1].strip(), line[2].strip()]
                elif len(line) == 2:
                    self.amp_mod[name_funct] = [line[1].strip()]
                elif len(line) == 1:
                    self.amp_mod[name_funct] = None
    
    def read_notes(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            start = ''
            for line in lines:
                info = line.split()
                start = float(info[0])
                note = info[1]
                duration = float(info[2])
                
    def sinoidal(self, frec, mult, inte, duration):
        for i in range(mult):
            calc = inte * np.sin(2*np.pi*frec*mult*duration)
        return calc
    plt.plot(sinoidal(4186.01, 4,0.72727272,0.5))










