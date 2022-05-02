from Manejador import Manejador
from Registro import Registro
import os

if __name__ == "__main__":
    m = Manejador()
    m.cargar()
    m.mostrarlista()

    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Mostrar para cada variable el día y hora de menor y mayor valor.")
        print("[2] Indicar la temperatura promedio mensual por cada hora.")
        print("[3] Dado un número de día listar los valores de las tres variables para cada hora del día dado.")
        print("[0] Para SALIR del menu")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))
            print("Se muestra para cada variable el día y hora de menor y mayor valor.\n")
            print(m.opcion1())
        elif(op == 2):
            acum = int(input("La temperatura promedio mensual por cada hora.\n"))
            #Viajero.acumularMillas(acum)
        elif(op == 3):
            print("Ingrese el día a buscar: ")
            dia = int(input())
            canje = int(input("Lista de los valores de las tres variables para cada hora del día {}.\n".format(dia)))
            #Viajero.canjearMillas(canje)
        elif(op == 0):
            continuar = not continuar
