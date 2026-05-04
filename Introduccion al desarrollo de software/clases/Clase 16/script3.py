# Autor: David Cañaveral Lopera
# Fecha: 29/04/2026
# Version: 2.0
# Descripcion:  Elabora un pseudo codigo que calcule el promedio de los puntajes, el numero de puntajes mayores a 80 y el numero de puntajes menores a 80.

puntajes_estudiantes = []
contador_menores = 0 
contador_mayores = 0
acumulador_puntajes = 0   
iterador = 0 
valor_ingresado = ''

while iterador < 10:
    iterador += 1
    valor_ingresado = input(f'Ingrese el puntaje del estudiante numero {iterador}: ')
    if valor_ingresado.isalpha():
        print("El valor ingresado no es numerico")
        iterador -= 1
    else:           
        puntajes_estudiantes.append(int(valor_ingresado))

        acumulador_puntajes += puntajes_estudiantes[iterador-1]

        if puntajes_estudiantes[iterador-1] >= 80: contador_mayores +=1
        if puntajes_estudiantes[iterador-1] < 80: contador_menores +=1     

promedio_puntajes = acumulador_puntajes / len(puntajes_estudiantes)

print(f'Numero de porcentajes mayores o iguales a 80: {contador_mayores}')
print(f'Numero de porcentajes menores a 80: {contador_menores}')
print(f'Promedio de puntajes: {promedio_puntajes}')


