import os, msvcrt
import csv
from funciones import *

delivery=[]
deliverys=[]
while True:
    print("   |GAXPLOSIVE|")
    print("1.Registrar pedido\t2.Listar todos los pedidos\t3.Buscar pedido por RUT\t4.Imprimir hoja de ruta\t5.Salir del programa")
    opc = int(input("Ingrese una opcion: "))
    os.system('cls')
    if opc == 1:
        datos_de_compra()
    elif opc == 2:
        lista_de_pedidos()
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    else:
        print("Adios :)")