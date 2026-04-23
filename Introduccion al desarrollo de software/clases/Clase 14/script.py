# Autor: David Canaveral
# Versión: 1.0
# Fecha: 15/04/2026
# Descripcion: Algoritmo que calcule la temperatura promedio de las lecturas enviadas por un sensor mientras que no exceda los 30°C

# Importación de librerias
import time

# definicion de variables
TEMPERATURA_MAXIMA = 30 
contador_temperaturas = 0
acumulador_temperaturas = 0
temperatura_actual = 0 

# Mensajes de muestra
print('--------------> SIATA <--------------\n \n')
print('-> Envio de data cada 120 minutos\n \n')
time.sleep(2)

# definicon del ciclo while de cumplimiento hasta encontrar temperaturas anormales
while (temperatura_actual <= TEMPERATURA_MAXIMA):
    # lectura de datos
    temperatura_actual = float(input("Ingrese la temperatura actual \n-> "))
    contador_temperaturas += 1 # contador general 
    acumulador_temperaturas += temperatura_actual # suma de todas las temperaturas

promedio_temperaturas = acumulador_temperaturas / contador_temperaturas # calculo del promedio 

print("<------------------------------------->\n \n-> Se superó el limite de temperatura permitido\n -------------")
time.sleep(1)   
print('--------------> Reporte <--------------\n \n')    
time.sleep(2)    

# muestreo de datos
print(f"El promedio de temperaturas es: {promedio_temperaturas}°")

print(f"La cantidad de temperaturas fue: {contador_temperaturas}")