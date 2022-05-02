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
                print(self.__lista[dia][hora])
            print()
        print()
    
    def cargar(self):
        archivo = open("datos.csv")
        lector = csv.reader(archivo,delimiter=";")
        cabecera = True
        for fila in lector:
            if cabecera:
                cabecera = not cabecera
                continue
            dia = int(fila[0])
            hora = int(fila[1])
            temperatura = float(fila[2])
            humedad = float(fila[3])
            presion = float(fila[4])
            self.__lista[dia][hora] = Registro(temperatura, humedad, presion)
        archivo.close()
    
    #opcion1
    def opcion1(self):
        maxTemp = 0
        minTemp = 99
        maxHum = 0
        minHum = 99
        maxPres = 0
        minPres = 99
        for dia in range(30):
            for hora in range(24):
                if self.__dia[dia][hora].getTemperatura() > maxTemp:
                    maxTemp = self.__dia[i][hora].getTemperatura()
                    maxTempDia = dia
                    maxTempHora = hora
                if self.__dia[dia][hora].getTemperatura() < minTemp:
                    minTemp = self.__dia[dia][hora].getTemperatura()
                    minTempDia = dia
                    minTempHora = hora
                if self.__dia[dia][hora].getHumedad() > maxHum:
                    maxHum = self.__dia[dia][hora].getHumedad()
                    maxHumDia = dia
                    maxHumHora = hora
                if self.__dia[dia][hora].getHumedad() < minHum:
                    minHum = self.__dia[dia][hora].getHumedad()
                    minHumDia = dia
                    minHumHora = hora
                if self.__dia[dia][hora].getPresion() > maxPres:
                    maxPres = self.__dia[dia][hora].getPresion()
                    maxPresDia = dia
                    maxPresHora = hora
                if self.__dia[dia][hora].getPresion() < minPres:
                    minPres = self.__dia[dia][hora].getPresion()
                    minPresDia = dia
                    minPresHora = hora
        print("La temperatura más alta fue de {} grados en el día {} a las {} horas.".format(maxTemp, maxTempDia, maxTempHora))
        print("La temperatura más baja fue de {} grados en el día {} a las {} horas.".format(minTemp, minTempDia, minTempHora))
        print("La humedad más alta fue de {} % en el día {} a las {} horas.".format(maxHum, maxHumDia, maxHumHora))
        print("La humedad más baja fue de {} % en el día {} a las {} horas.".format(minHum, minHumDia, minHumHora))
        print("La presión más alta fue de {} en el día {} a las {} horas.".format(maxPres, maxPresDia, maxPresHora))
        print("La presión más baja fue de {} en el día {} a las {} horas.".format(minPres, minPresDia, minPresHora))
