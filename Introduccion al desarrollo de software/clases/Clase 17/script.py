'''
Autor: David Cañaveral 
Versión: 1.0
Fecha: 04/05/2026
Descripción: 
Contruye un script de python que lea 2 numeros enteros positivos y que calcule para ellos la suma la multiplicación y la división 
'''

# Proceso
def suma(n1,n2):
    return n1 + n2
def multiplicacion(n1,n2):
    return n1 * n2
def division(n1,n2):
    return "Valor del denominador es 0 por lo tanto la operacion no es valida" if n2 == 0 else n1 / n2

def main():
    # Datos de entrada
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo número: "))
    # Proceso
    if (primer_numero >= 0 and segundo_numero >= 0 ):
        print(f'Suma: {suma(primer_numero,segundo_numero)}')
        print(f'Multiplicacion: {multiplicacion(primer_numero,segundo_numero)}')
        print(f'Division: {division(primer_numero,segundo_numero)}')
    else:
        print('Los numeros para las operaciones deben ser positivos')    

if __name__ == "__main__":
    main()
    