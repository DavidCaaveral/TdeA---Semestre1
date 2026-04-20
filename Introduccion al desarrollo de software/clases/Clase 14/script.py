# Autor: David Canaveral
# Versión: 1.0
# Fecha: 15/04/2026
# Descripcion: Algoritmo que calcule la temperatura promedio de las lecturas enviadas por un sensor mientras que no exceda los 30°C

TEMPERATURA_MAXIMA = 30 
contador_temperaturas = 0
acumulador_temperaturas = 0
temperatura_actual = 0 

while (temperatura_actual <= TEMPERATURA_MAXIMA):
    temperatura_actual = float(input("Ingrese la temperatura actual \n-> "))
    contador_temperaturas += 1
    acumulador_temperaturas += temperatura_actual

promedio_temperaturas = acumulador_temperaturas / contador_temperaturas

print("Se superó el limite de temperatura permitido\n -------------")

print(f"El promedio de temperaturas es: {promedio_temperaturas}°")

print(f"La cantidad de temperaturas fue: {contador_temperaturas}")