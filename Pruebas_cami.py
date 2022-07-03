import numpy as np
import matplotlib.pyplot as plt
from notes import notes_mapping

def sine_wave(harm: int, amplitude: float, dur: float, freq: float, start: float):
  x = np.linspace(start, start+dur, 1000)
  y = amplitude * np.sin(2*np.pi*freq*harm*(x-start))
  return y, x

def note_freq (note):
  for x in notes_mapping:
    if x[0] == note:
      freq = float(x[1])
      return freq

with open('instruments/piano.txt', 'r') as f:
  num_harmonics = f.readline().strip()
  harm_dict = {}
  amp_mod={} #modulador de amplitud

  for n in range(int(num_harmonics)):
    mult_harm =  f.readline()
    mult_harm = mult_harm.split(' ')
    harm_dict[float(mult_harm[0])] = float(mult_harm[1].strip('\n'))
  
  for amp in range(3): # 3 = len(filename) - num_armonics - 1
    line = f.readline().split(" ")
    name_funct = line[0].strip()
    if len(line) == 2:
        amp_mod[name_funct] = line[1].strip()
    elif len(line) == 1:
        amp_mod[name_funct] = None

with open("scores/escala.txt", 'r') as f:
  lines= f.readlines()
  for line in lines:
    info = line.split()
    start = float(info[0])
    note = info[1]
    if 's' in note:
      note = note [0] + note [2]
      freq = note_freq(note)
      freq = freq * (1.0594623)
    else:
      freq = note_freq (note)
    duration = float(info[2])
    func_sum = 0
    for harm in harm_dict.keys():
      sen, x = sine_wave(harm, harm_dict[harm], duration, freq, start)
      func_sum += sen
    


plt.plot(x, func_sum)
plt.show ()

