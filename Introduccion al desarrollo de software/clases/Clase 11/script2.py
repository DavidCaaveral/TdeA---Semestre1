# Autor: David Cañaveral
# Version: 1.0
# Fecha: 30/03/2026
# Descripcion: Programa que muestre un "Hola" si la contraseña es correcta

CONSTCLAVE = 1234 #inicializar constante
clave = 0 #inicializar variable

while clave != CONSTCLAVE:
    clave = int(input("Ingrese PIN: "))
    
print("clave correcta!!")    

# ES INDETERMINADO PORQUE EN TEORIA SE PUEDE REPETIR DE MANERA INFINITA HASTA QUE SE CUMPLA LA CONDICION