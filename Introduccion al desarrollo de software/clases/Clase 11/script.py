# Autor: David Cañaveral
# Version: 1.0
# Fecha: 18/03/2026
# Descripcion: Programa que muestre en pantalla los numeros pares del 0 al 10

import time

contador_pares=0 # declaración de un contador
for numero_par in range(11):
    if(numero_par % 2 == 0):
        print(numero_par)
        contador_pares += 1

time.sleep(1)

print(f" \nLos pares hallados fueron: {contador_pares}")        


