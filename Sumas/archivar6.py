__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'

import wave
import struct


class Archivo6:
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre

    def archivar6(self, datos1,datos2,datos3,datos4):
        output = wave.open(self.nombre, 'w')
        Set_Bits = self.bits/8
        output.setparams((2, Set_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))
        values1 = []
        for i in range(0, len(datos1)):
            packed_value1 = struct.pack('<h', datos1[i])
            values1.append(packed_value1)
            packed_value2 = struct.pack('<h', datos4[i])
            values1.append(packed_value2)
        for i in range(0, len(datos2)):
            packed_value1 = struct.pack('<h', datos4[i])
            values1.append(packed_value1)
            packed_value2 = struct.pack('<h', datos2[i])
            values1.append(packed_value2)
        for i in range(0, len(datos3)):
            packed_value3 = struct.pack('<h', datos3[i])
            values1.append(packed_value3)
            packed_value3 = struct.pack('<h', datos3[i])
            values1.append(packed_value3)
        value_str = ''.join(values1)
        output.writeframes(value_str)
        output.close()