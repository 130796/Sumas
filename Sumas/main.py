___author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz_Corregido'


import sys
from Tkinter import*
from Open import Open
import pyaudio
import wave
from ejercicio1class import Seno
from archivar import Archivo1
from archivar2 import Archivo2
from archivar3 import Archivo3
from archivar4 import Archivo4
from archivar5 import Archivo5
from archivar6 import Archivo6
from archivar7 import Archivo7

import time
import Tkinter as Tk

def main():
    raiz= Tk.Tk()
    raiz.title("Program")
    CHUNK = 1024
    #Pide nombre de archivo.wav
    x1=Label(raiz, fg="black")
    x1.config(text="Nombre del archivo que desea generar")
    x1.pack()
    x3 = Entry(raiz)
    x3.pack()
    #Guarda, abre y reproduce archivo.wav de primera suma
    Archivo = Open(CHUNK)
    def play_audio1():
        onda = Seno(44100, 16,90,23000)
        datos1 = onda.generarSeno(450)
        datos2 = onda.generarSeno(1000)
        archivo = Archivo1(44100, 16, x3.get())
        archivo.archivar(datos1,datos2)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Primera Suma",width=15,command=play_audio1)
    x6.pack()
    #Guarda, abre y reproduce archivo.wav de segunda suma
    def play_audio2():
        onda = Seno(44100, 16,90,23000)
        datos1 = onda.generarSeno(450)
        datos2 = onda.generarSeno(1000)
        archivo = Archivo2(44100, 16, x3.get())
        archivo.archivar2(datos1,datos2)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Segunda Suma",width=15,command=play_audio2)
    x6.pack()
    #Guarda, abre y reproduce archivo.wav de tercera suma
    def play_audio3():
        onda = Seno(44100, 16,30,23000)
        datos1 = onda.generarSeno(500)
        datos2 = onda.generarSeno(1000)
        datos3 = onda.generarSeno(300)
        datos4 = onda.generarSeno(700)
        archivo = Archivo3(44100, 16, x3.get())
        archivo.archivar3(datos1,datos2,datos3)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Tercera Suma",width=15,command=play_audio3)
    x6.pack()
    #Guarda, abre y reproduce archivo.wav de Cuarta suma
    def play_audio4():
        onda = Seno(44100, 16,30,23000)
        datos1 = onda.generarSeno(500)
        datos2 = onda.generarSeno(1000)
        archivo = Archivo4(44100, 16, x3.get())
        archivo.archivar4(datos1,datos2)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Cuarta Suma",width=15,command=play_audio4)
    x6.pack()
    #Guarda, abre y reproduce archivo.wav de quinta suma
    def play_audio5():
        onda = Seno(44100, 16,30,23000)
        datos1 = onda.generarSeno(500)
        datos2 = onda.generarSeno(1000)
        datos3 = onda.generarSeno(700)
        archivo = Archivo5(44100, 16, x3.get())
        archivo.archivar5(datos1,datos2,datos3)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Quinta Suma",width=15,command=play_audio5)
    x6.pack()
    #Guarda, abre y reproduce archivo.wav de sexta suma
    def play_audio6():
        onda = Seno(44100, 16,30,23000)
        datos1 = onda.generarSeno(500)
        datos2 = onda.generarSeno(1000)
        datos3 = onda.generarSeno(700)
        datos4 = onda.generarSeno(0)
        archivo = Archivo6(44100, 16, x3.get())
        archivo.archivar6(datos1,datos2,datos3,datos4)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Sexta Suma",width=15,command=play_audio6)
    x6.pack()
    #Guarda, abre y reproduce archivo.wav de septima suma
    def play_audio7():
        onda = Seno(44100, 16,30,23000)
        datos1 = onda.generarSeno(500)
        datos2 = onda.generarSeno(1000)
        datos3 = onda.generarSeno(700)
        archivo = Archivo7(44100, 16, x3.get())
        archivo.archivar7(datos1,datos2,datos3)
        Archivo.ruta = x3.get()
        t3 = Archivo.abrir()
        Archivo.inicio(t3[0],t3[1],t3[2])
        Archivo.reproducir()

    x6=Button(raiz,text="Septima Suma",width=15,command=play_audio7)
    x6.pack()

    raiz.mainloop()




if __name__ == "__main__":
    main()