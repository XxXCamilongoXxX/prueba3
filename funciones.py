#funciones
import os, msvcrt
delivery=[]
deliverys=[]
def datos_de_compra():
        RUT = int(input("Ingrese su rut(EJ:11111111): "))
        if RUT < 11111111 or RUT > 99999999:
            print("Ingrese un rut valido!")
        else:
            pass
        delivery.append(RUT)
        Nombre = input("Ingrese su nombre: ")
        delivery.append(Nombre)
        Direccion = input("Ingrese su dirección: ")
        delivery.append(Direccion)
        Comuna = input("Ingrese su comuna: ")
        delivery.append(Comuna)
        os.system('cls')
        Compra = int(input("Que cilindro desea comprar(5kg,15kg): "))
        if Compra == 5:
            cilindro5kg = int(input("Cuantos desea llevar: "))
            if cilindro5kg <=0:
                print("Ingrese cantidad valida")
            else:
                print("Se añadieron ",cilindro5kg,"cilindros de 5kg")
                delivery.append(cilindro5kg)
                print("RUT Cliente Dirección Comuna CIL.5KG CIL.15KG")
                print(delivery)
                deliverys.append(delivery)
        elif Compra == 15:
            cilindro15kg = int(input("Cuantos desea llevar: "))
            if cilindro15kg <=0:
                print("Ingrese cantidad valida")
            else:
                print("Se añadieron ",cilindro15kg,"cilindros de 15kg")
                delivery.append(cilindro15kg)
                print("RUT Cliente Dirección Comuna CIL.5KG CIL.15KG")
                print(delivery)
                deliverys.append(delivery)
        else:
            print("Ingrese opcion valida!")
def lista_de_pedidos():
    print("|Lista de pedidos|")
    print(deliverys)