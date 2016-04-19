___author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz_Corregido'
import math
import wave
import pyaudio

class Seno:
        wavearray = []
        def __init__(self, sampling, bits,bpm,max):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.tamano = ((sampling *60)/bpm)
            self.max=max
        def generarSeno(self,Frecuencia1):

            wavearray = []
            for i in range(0, self.tamano):

                    datos = self.max*math.sin((2*math.pi*Frecuencia1*i)/self.SamplingRate)
                    wavearray.append(datos)

            return wavearray
