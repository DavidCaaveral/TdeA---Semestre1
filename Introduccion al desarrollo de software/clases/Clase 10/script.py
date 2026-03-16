# DATOS AMBIENTALES
# Autor: David Cañaveral
# Version: 1.0
# Descripcion: Datos Ambientales
import time
temperature = 0
flag = "si"

print("-------> Sensor de Temperatura <-------")
print("")
while flag == "si":
    temperature = float(input("Ingrese la temperatura registrada\n"))
    print("")
    print("-------> Determinando <-------")
    time.sleep(3) # para que espere 3 segundod
    print("")
    if (temperature < 0):
        print(f"La temperatura registrada es negativa con valor de {temperature}°")
    elif(temperature > 0):
        print(f"La temperatura registrada es positiva con valor de {temperature}°")
    else:
        print("Tu temperatura registró 0") 

    print("")       
    flag = str(input("desea ingresar otra temperatura?\n")).lower() 

print("Hasta pronto 👍")
