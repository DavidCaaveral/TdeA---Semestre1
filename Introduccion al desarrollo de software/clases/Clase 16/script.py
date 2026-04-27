# Autor: David Cañaveral
# Fecha: 27/04/2026
# Version: 1.0
# Descripcion: Elabora un pseudo codigo que calcule el promedio de los puntajes, el numero de puntajes mayores a 80 y el numero de puntajes menores a 80.

puntajes_estudiantes = [120,93,70,45,99,86,83,100,80,85]

contador_menores = 0 
contador_mayores = 0
acumulador_puntajes = 0 
NUMERO_PUNTAJES = len(puntajes_estudiantes)

for i in puntajes_estudiantes:
    acumulador_puntajes += i

    if i >= 80: contador_mayores +=1 
    if i < 80: contador_menores +=1 

promedio_puntajes = acumulador_puntajes / NUMERO_PUNTAJES

print(f'Numero de porcentajes mayores o iguales a 80: {contador_mayores}')
print(f'Numero de porcentajes menores a 80: {contador_menores}')
print(f'Pormedio de puntajes: {promedio_puntajes}')