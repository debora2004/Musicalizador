import numpy as np
import modulatorfunctions
import matplotlib.pyplot as plt
from notes import notes_mapping
filename_notes = "scores/escala.txt"
filename_instruments = 'instruments/piano.txt'

class Synthesizer:
  def __init__(self, harm_dict, amplitude_mod: dict , filename_notes): # recibe un instrumento y una partitura
    self.harm_dict=harm_dict #lista de largo n, compuesta por los n armónicos del instrumento recibido
    self.filename_notes = filename_notes
    self.functions = amplitude_mod.keys() # [0] es la funcion de attack, [1] la de sustain y [2] la de decay
    self.parameters = amplitude_mod.values() # [0] son parametros de attack, [1] de sustain y [2] de decay
  
  def read_notes (self):
    with open(self.filename_notes, 'r') as f:
      lines= f.readlines()
      for line in lines:
        info = line.split()

        start = float(info[0])
        note = info[1]
        duration = float(info[2])

        freq = self.frequency (note)

        x, harm_sum = self.harm_sum(duration, freq, start)
        plt.plot(x, harm_sum)

  def sine_wave(self, harm: int, amplitude: float, dur: float, freq: float, start: float):
    x = np.linspace(start, start+dur, 1000)
    y = amplitude * np.sin(2*np.pi*freq*harm*(x-start))
    return x, y

  def note_freq (self, note):
    for x in notes_mapping:
      if x[0] == note:
        freq = float(x[1])
        return freq

  def frequency (self, note):
    if 's' in note:
        note = note [0] + note [2] #Elimina s de la nota: As4 -> A4
        freq = self.note_freq(note)
        freq = freq * (1.0594623)
    else:
      freq = self.note_freq (note)
    return freq

  def harm_sum (self, duration, freq, start):
    '''Suma de los armonicos a cada nota'''
    harm_sum = 0
    for harm in harm_dict.keys():
      x, sen = self.sine_wave(harm, harm_dict[harm], duration, freq, start)
      harm_sum += sen
    return x, harm_sum

 #///PARTE DE MODULACION POR FLOR///

  def modulacion(self, t, t0, ta, td,d): # fa,fs,fd son las funciones de mod_amp
                                          # ta tiempo de ataque, td tiempo de decaimiento, 
                                          # t0 es el instante en el que inicia, d es la duracion
    if t0 < t and t < (t0+ta):
      result = self.amp_mod('attack', (t-t0))
    elif (t0+ta) < t and t < (t0+d):
      result = self.amp_mod('sustain', (t-(t0+ta)))
    elif (t0+d) < t and t < (t0+d+td):
      result = self.amp_mod('sustain', (t0+d))*self.amp_mod("decay", (t-(t0+d)))
    else:
      result = 0
    return result
      
  def amp_mod(self, types:str, t):
    if types=="attack":
      i=0
    elif types=="sustain":
      i=1
    elif types=="decay":
      i=2
    function, parameter = self.functions[i], self.parameters[i]
    result=modulatorfunctions.ModulatorFunctions(function, parameter, types)
    return result

  def amplitud(self, t, A):
    result = A*self.sinoidal*self.modulacion
    return result

#///ABRIMOS EL INSTRUMENTO///
with open(filename_instruments, 'r') as f:
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
    if len(line) > 1:
        amp_mod[name_funct] = line[1].strip()
    elif len(line) == 1:
        amp_mod[name_funct] = None
