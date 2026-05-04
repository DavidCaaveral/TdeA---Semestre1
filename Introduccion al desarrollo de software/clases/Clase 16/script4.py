# Autor: David Cañaveral
# Versión: 3.0
# Fecha: 05/04/2026
# Descripción: Algoritmo que calcula el promedio de temperaturas usando listas

# Importacion de librerias
import time

# Definicion de constantes
TEMPERATURA_MAXIMA = 26 
TEMPERATURA_MINIMA = 16
TOTAL_TEMPERATURAS = 12

# Definicion de variables
contador_mayor = 0
contador_menor = 0 
contador_normales = 0  
acumulador_general = 0

# Lista para almacenar temperaturas
lista_temperaturas = []

# Mensajes de muestra
print('--------------> SIATA <--------------\n')
print('-> Envio de data cada 120 minutos\n')
time.sleep(2)

# Inicio del ciclo
for iterador in range(TOTAL_TEMPERATURAS):

    temperatura_actual = float(input(f"Ingrese la temperatura #{iterador + 1}: "))

    # Guardar en la lista
    lista_temperaturas.append(temperatura_actual)

    # Acumulador
    acumulador_general += temperatura_actual

    # Clasificacion
    if temperatura_actual >= TEMPERATURA_MAXIMA:
        contador_mayor += 1
    elif temperatura_actual <= TEMPERATURA_MINIMA:
        contador_menor += 1
    else:
        contador_normales += 1

# Calculo del promedio
promedio_temperaturas = acumulador_general / TOTAL_TEMPERATURAS

# Reporte
print('\n--------------> Reporte <--------------\n')
time.sleep(2)