# Autor: David Cañaveral
# Version: 1.0
# Descripcion: Numero magico
import random
MAGICNUM = 20
# MAGICNUM = random.randint(1,10) # si se requiere que el numero sea un random, activar constante
flag = False
print("------NUMERO MAGICO-----")
print("")
nombreLudo = input("Ingrese su nombre \n")
print("")
print("---------------------")
print("")

for i in range(3):
    numeroLudo = int(input(f"{nombreLudo} ingrese el numero ente 1 y 100 \n"))
    if numeroLudo > 100 or numeroLudo < 1:
        print("El numero se encuentra fuera de rango, por favor ingrese uno entre 1 y 100")
        print("")
        print("---------------------")
        print("")
    else:    
        if numeroLudo == MAGICNUM:
            print("EL NUMERO ES CORRECTO") 
            print("")
            print("---------------------")
            print("")
            flag = True
        elif numeroLudo > MAGICNUM:
            print("El numero es mayor al numero magico")
            print("")
            print("---------------------")
            print("") 
        else:
            print("El numero es menor al numero magico")
            print("")
            print("---------------------")
            print("")        

    