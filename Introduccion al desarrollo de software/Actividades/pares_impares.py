# Autor: David Cañaveral
# Version: 1.0
# Fecha: 06/04/2026
# Descripción: script que calcula el numero y la suma de los numeros pares e impares en el rango 0 a 10
# Declaración de variables 
contador_impar = 0
suma_impar = 0 
contador_par = 0
suma_par = 0
# USO ESTRICTO DE SNAKECASE

for numero_iterado in range(0,11):
    if (numero_iterado % 2 == 0):
        contador_par += 1
        suma_par += numero_iterado 
        print(f'el numero par: {numero_iterado}')
    else:
        contador_impar += 1    
        suma_impar += numero_iterado
        print(f'el numero impar: {numero_iterado}')

print(f'\ncantidad pares: {contador_par}\n')
print(f'suma de pares: {suma_par}\n')        
print(f'cantidad impares: {contador_impar}\n')
print(f'suma de impares: {suma_impar}\n')        