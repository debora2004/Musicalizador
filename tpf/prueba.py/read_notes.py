import notes
import math
import matplotlib.pyplot as plt
import numpy as np


notes = notes.notes_mapping 

def sinoidal(frec,mult,inte,duration):
    calc = 0
    for i in range(mult):
      calc = inte * np.sin(2*np.pi*frec*mult*duration)
    return calc
#plt.plot(sinoidal(4186.01, 4,0.72727272,0.5))

with open('piano.txt', 'r') as f:
    num_harmonics = f.readline().strip()
    harm_list = {}
    amp_mod={} #modulador de amplitud


    for n in range(int(num_harmonics)):
        mult_harm =  f.readline()
        mult_harm = mult_harm.split(' ')
        harm_list[mult_harm[0]] = mult_harm[1].strip('\n')
        #print(harm_list)
    
    for amp in range(3):    # 3 = len(filename) - num_armonics - 1
        line = f.readline().split(" ")
        name_funct = line[0].strip()
        if len(line) == 4:
            amp_mod[name_funct] = (line[1].strip(), line[2].strip(), line[3].strip())
        elif len(line) == 3:
            amp_mod[name_funct] = (line[1].strip(), line[2].strip())
        elif len(line) == 2:
            amp_mod[name_funct] = line[1].strip()
        elif len(line) == 1:
            amp_mod[name_funct] = None
    print('moduladroes de amplitud: ', amp_mod)
    print('lista de armonicos: ', harm_list)

with open("escala_01.txt", 'r') as f:
    lines= f.readlines()
    start = ''
    for line in lines:
        info = line.split()
        start =float(info[0])
        note= info[1]
        duration = float(info[2])
        #print(start)
        #print(note)
        #print(duration)
        #print(' ')
        
       


