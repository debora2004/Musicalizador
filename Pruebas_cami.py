import numpy as np
import modulatorfunctions
import matplotlib.pyplot as plt
from notes import notes_mapping
filename_notes = "scores/escala.txt"
filename_instruments = 'instruments/piano.txt'
'''
class Synthesizer:
  def __init__(self, harm_dict, amplitude_mod: dict , filename_notes, sps): # recibe un instrumento y una partitura
    self.harm_dict=harm_dict #lista de largo n, compuesta por los n armónicos del instrumento recibido
    self.sps = sps 
    self.filename_notes = filename_notes
    self.functions = amplitude_mod.keys() # [0] es la funcion de attack, [1] la de sustain y [2] la de decay
    self.parameters = amplitude_mod.values() # [0] son parametros de attack, [1] de sustain y [2] de decay
  
  def read_notes (self):
      with open(self.filename_notes, 'r') as f:
        #aca llamar a funcion que encuentre el largo de la funcion y cree el array de ceros con eso
        lines= f.readlines()
        ultra_info = []
        for line in lines:
          info = line.split()
          ultra_info.append ( (float(info[0]), info[1], float(info[2])) )
      return ultra_info
  
  def get_song_length (self):
    read = self.read_notes()
    f_position = len(read) - 1
    f_note = read(f_position) #Los datos de la ultima nota
    length_time = f_note[0] + f_note [2]  #Start + duracion
    return length_time

  def signal_generator (self):
    read = self.read_notes()
    for a in read:
      start = a[0]
      note = a[1]
      duration = a[2]
      freq = self.frequency (note)
      harm_sum = self.harm_sum(duration, freq, start)
      # vamos a tener que hacer la modulacion de amplitud de la nota (queda mod_sine)
      mod_sine = self.mod ()
      # Esa senoidal final es la que se suma en el array de ceros
      temp_array = self.array_sum(start, duration, mod_sine, temp_array)
    return temp_array #(Signal)

    #plt.plot(x, harm_sum)
    #plt.show()

    # Necesito song_len
    # No se como hacer que la definicion del array de ceros funcione sin que lo tengan que llamar y la asignacion al self se haga sola
  def zero_array(self, song_len):
    a = np.zeros(int(self.spssong_len))
    return a

    # Se tiene que haber creado el array de ceros antes de esta llamada/antes del for en el que se recorren las notas
    # Estaba pensando en poner el zero_ar como un atributo de el sintetizador, asi el valor cambia al llamar a la funcion y no necesita retornar nada
  def array_sum (self, start, dur, waveform, temp_array):
    end = start + dur
    temp_array[int(self.spsstart) : int(self.sps*end)] += waveform # Waveform es la senoidal final de la nota
    return temp_array

  def sine_wave(self, harm: int, amplitude: float, dur:float, freq: float):
    """Creates the sine wave of a note
    harm: the number that multiplies the frequency of the base note, to get the frequency of the overtone
    amplitude: the intensity of the overtone. Must be between 0 and 1
    freq: the frequency of the base note

    returns y: the sine_wave of the note
    """
    y = amplitude * np.sin(2* np.pi * freq * harm * np.arange(self.sps*dur)/self.sps)
    return y

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
    #Suma de los armonicos a cada nota
    harm_sum = 0
    for harm in harm_dict.keys():
      sen = self.sine_wave(harm, harm_dict[harm], duration, freq, start)
      harm_sum += sen
    return harm_sum

class Modular():
  def __init__ (self, time, start, t_a, t_d, duration):
    self.t = time
    self.t0 = start
    self.ta = t_a
    self.td = t_d
    self.d = duration
  

  def mod(self): # fa,fs,fd son las funciones de mod_amp
                                            # ta tiempo de ataque, td tiempo de decaimiento, 
                                            # t0 es el instante en el que inicia, d es la duracion
      t = self.t 
      t0 = self.t0 
      ta = self.ta 
      td = self.td
      d = self.d
      f_attack = np.where( (t>t0) & (t<(t0+ta)) )
      f_sustain = np.where( (t>(t0+ta)) & (t<(t0+d)) )
      f_combo = np.where( (t>(t0+d)) & (t<(t0+d+td)) )

      # if t0 < t and t < (t0+ta):
      #   result = self.amp_mod('attack', (t-t0))
      # elif (t0+ta) < t and t < (t0+d):
      #   result = self.amp_mod('sustain', (t-(t0+ta)))
      # elif (t0+d) < t and t < (t0+d+td):
      #   result = self.amp_mod('sustain', (t0+d))*self.amp_mod("decay", (t-(t0+d)))
      # else:
      #   result = 0
      # return result
        
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

t = np.arange(sps*1.5)
t0 = 0
ta = 0.05
td = 0.02
d = 20
a = Modular(t, t0, ta, td, d)
a.mod()
'''

filename_notes = 'scores/escala.txt'

def read_notes():
  with open(filename_notes, 'r') as f:
    #aca llamar a funcion que encuentre el largo de la funcion y cree el array de ceros con eso
    lines= f.readlines()
    ultra_info = []
    for line in lines:
      info = line.split()
      ultra_info.append ( (float(info[0]), info[1], float(info[2])) )
  return ultra_info

def array_sum (a, temp_array):
  temp_array += a
  return temp_array
    
gg = 0
read = read_notes()
array_list = []
for a in read:
  b = a[2]
  temp_array = array_sum (b, gg)
  array_list.append(temp_array)
final_array = sum(array_list)
print (final_array)

