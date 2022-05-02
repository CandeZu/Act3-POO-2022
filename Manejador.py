from Registro import Registro
import csv

class Manejador:
    __lista = []

    def __init__(self):
        for i in range(30):
            self.__lista.append([])
            for j in range(24):
                registro = Registro(0,0,0)
                self.__lista[i].append(registro)
    
    def mostrarlista(self):
        for dia in range(30):
            for hora in range(24):
                print(self.__lista[dia][hora], end=" ")
            print()
        print()
    
    def cargar(self):
        archivo = open("datos.csv")
        lector = csv.reader(archivo)
        cabecera = True
        if cabecera:
            cabecera = not cabecera
        for fila in lector: