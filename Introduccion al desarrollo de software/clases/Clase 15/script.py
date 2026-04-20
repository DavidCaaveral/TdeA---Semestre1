# Autor: David Cañaveral
# Versión: 2.0
# Fecha: 04/20/2026
# Descripción:  Algoritmo que calcule la temperatura promedio de las lecturas enviadas por un sensor mientras que no exceda los 26°C

TEMPERATURA_MAXIMA = 26 
TEMPERATURA_MINIMA = 16
TOTAL_TEMPERATURAS = 12
contador_mayor = 0
contador_menor = 0 
contador_normales = 0  
acumulador_general = 0

for iterador in range(TOTAL_TEMPERATURAS):
    temperatura_actual = float(input("Ingrese la temperatura actual \n-> "))
    acumulador_general += temperatura_actual
    if temperatura_actual >= TEMPERATURA_MAXIMA:
        contador_mayor += 1
    elif temperatura_actual <= TEMPERATURA_MINIMA:
          contador_menor += 1
    else:
        contador_normales += 1

promedio_temperaturas = acumulador_general / TOTAL_TEMPERATURAS
        
print(f"El promedio de temperaturas es: {promedio_temperaturas}° \n ")

print(f"La cantidad de temperaturas normales fue: {contador_normales}")       
print(f"La cantidad de temperaturas superiores al limite fue: {contador_mayor}")       
print(f"La cantidad de temperaturas inferiores al limite fue: {contador_menor}")       
              
