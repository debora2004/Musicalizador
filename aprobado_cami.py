import numpy as np
from scipy.io.wavfile import write
from instrumento import Instrument
import modulatorfunctions
import matplotlib.pyplot as plt
from notes import notes_mapping
filename_notes = "scores/escala.txt"
filename_instruments = 'instruments/piano.txt'

inst = Instrument(filename_instruments)
harm_dict, amp_dict = inst.read_instrument()

class Synthesizer:
  def __init__(self, harm_dict: dict, amplitude_mod: dict , filename_notes: str, sps: float): # recibe un instrumento y una partitura
    self.harm_dict=harm_dict #lista de largo n, compuesta por los n armónicos del instrumento recibido
    self.sps = sps 
    self.filename_notes = filename_notes

    self.functions = amplitude_mod.keys() # [0] es la funcion de attack, [1] la de sustain y [2] la de decay
    self.parameters = list(amplitude_mod.values()) # [0] son parametros de attack, [1] de sustain y [2] de decay
  
  def read_notes (self):
      with open(self.filename_notes, 'r') as f:
        #aca llamar a funcion que encuentre el largo de la funcion y cree el array de ceros con eso
        lines= f.readlines()
        ultra_info = []
        for line in lines:
          info = line.split()
          ultra_info.append ( (float(info[0]), info[1], float(info[2])) )
      return ultra_info
  
  def get_song_len (self):
    read = self.read_notes()
    f_position = len(read) - 1
    f_note = read[f_position] #Los datos de la ultima nota
    song_len = f_note[0] + f_note [2]  #Start + duracion
    return song_len

  def signal_generator (self):
    read = self.read_notes()
    song_len = self.get_song_len()
    zero_array = self.zero_array(song_len)
    array_list = []
    for a in read:
      start = a[0]
      note = a[1]
      duration = a[2]

      freq = self.frequency (note)
      harm_sum = self.harm_sum(duration, freq, start) #ESTO ES Y(T)
      
      ta, td = self.time_mod()
      t = np.arange(self.sps * song_len)

      #mod_sine = self.mod (t, start, ta, td, duration)
      temp_array = self.array_sum(start, duration, harm_sum, zero_array) #En vez de harm_sum deberia ser mod_sine
      array_list.append(temp_array)
    final_array = sum(array_list)
    return final_array #(Signal)

    # Necesito song_len
    # No se como hacer que la definicion del array de ceros funcione sin que lo tengan que llamar y la asignacion al self se haga sola
  def zero_array(self, song_len):
    a = np.zeros(int(self.sps*song_len))
    return a

    # Se tiene que haber creado el array de ceros antes de esta llamada/antes del for en el que se recorren las notas
    # Estaba pensando en poner el zero_ar como un atributo de el sintetizador, asi el valor cambia al llamar a la funcion y no necesita retornar nada
  def array_sum (self, start, dur, waveform, zero_array):
    end = start + dur
    zero_array[int(self.sps*start) : int(self.sps*end)] += waveform # Waveform es la senoidal final de la nota
    return zero_array

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
    '''Suma de los armonicos a cada nota'''
    harm_sum = 0
    for harm in self.harm_dict.keys():
      sen = self.sine_wave(harm, self.harm_dict[harm], duration, freq)
      harm_sum += sen
    return harm_sum

  def time_mod (self):
    ta = self.parameters[0][0]
    td = self.parameters[2][0]
    return ta, td

 #///PARTE DE MODULACION POR FLOR///

  def mod(self, t, t0, ta, td,d): # fa,fs,fd son las funciones de mod_amp
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


  #/////////////////////WAV
  def make_wav(self, name):
    """Creates and saves the .wav file
    final_sine: the function made from the sum of all of the notes in the song, with the respective amplitude modifiers.
    name: the name"""
    signal = self.signal_generator()
    signal = self.normalize (signal)
    waveform_ints = np.int16(signal * 32767)
    if ".wav" not in name:
      name += ".wav"
    write(name, self.sps, waveform_ints)
  
  def normalize (self, signal):
    signal += 32767 / np.max(np.abs(signal))
    return signal


sps = 44100
Syn = Synthesizer (harm_dict, amp_dict, filename_notes, sps)
Syn.make_wav('zzz')