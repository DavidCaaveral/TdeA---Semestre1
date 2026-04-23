# Autor: David Cañaveral
# Versión: 2.0
# Fecha: 04/20/2026
# Descripción:  Algoritmo que calcule la temperatura promedio de las lecturas enviadas por un sensor mientras que no exceda los 26°C

# Importacion de librerias
import time

# Dfinicion de variables
TEMPERATURA_MAXIMA = 26 
TEMPERATURA_MINIMA = 16
TOTAL_TEMPERATURAS = 12
contador_mayor = 0
contador_menor = 0 
contador_normales = 0  

acumulador_general = 0

# Mensajes de muestra
print('--------------> SIATA <--------------\n \n')
print('-> Envio de data cada 120 minutos\n \n')
time.sleep(2)

# inicio del ciclo for 
for iterador in range(TOTAL_TEMPERATURAS):
    # lectura de dato de temperaturas
    temperatura_actual = float(input("Ingrese la temperatura actual \n-> "))
    acumulador_general += temperatura_actual # suma de todas las temperaturas 

    if temperatura_actual >= TEMPERATURA_MAXIMA: # en caso de temperatura maxima
        contador_mayor += 1
    elif temperatura_actual <= TEMPERATURA_MINIMA: # en caso de temperatura minima
          contador_menor += 1
    else:
        contador_normales += 1 # en el resto de casos 

promedio_temperaturas = acumulador_general / TOTAL_TEMPERATURAS # calculo de promedio de temperaturas
      
print('--------------> Reporte <--------------\n \n')    
time.sleep(2)    

# muestreo de datos
print(f"El promedio de temperaturas es: {promedio_temperaturas}° \n ")

print(f"La cantidad de temperaturas normales fue: {contador_normales}")       
print(f"La cantidad de temperaturas superiores al limite fue: {contador_mayor}")       
print(f"La cantidad de temperaturas inferiores al limite fue: {contador_menor}")       
              
