__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'

import wave
import struct


class Archivo2:
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre

    def archivar2(self, datos1,datos2):
        output = wave.open(self.nombre, 'w')
        Set_Bits = self.bits/8
        output.setparams((1, Set_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))
        values1 = []
        for i in range(0, len(datos1)):
            packed_value1 = struct.pack('<h', datos1[i])
            packed_value2 = struct.pack('<h', datos2[i])
            values1.append(packed_value1)
            values1.append(packed_value2)


        value_str = ''.join(values1)
        output.writeframes(value_str)

        output.close()
