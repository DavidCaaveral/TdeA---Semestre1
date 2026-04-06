# Autor: David Cañaveral Lopera 
# Fecha: 30/03/2026
# version: 2.0
# Descripción: Verificar un numero magico 
import time

# Declaracion de variables
NUMERO_MAGICO = 73
keyboard_num = 0
person_name = ""
counter = 0 
flag = False

print("------------------------ \nEMPRESA DE LUDOPATAS ANTIOQUIA \n------------------------ \n ")
time.sleep(1)
print("------------------------ \n \nNUMERO MAGICO\n \n------------------------ \n ")
person_name = input("- Ingrese su nombre por favor \n-> ").strip().upper()
print(f" \n------------------------ \nINSTRUCCIONES PARA {person_name} \n  1. Ingrese cualquier numero del rango de 1 a 100 \n  2. Cuenta con tres oportunidades para adivinar el numero \n  3. Se le dará una pista del numero solo hasta el tercer intento \n------------------------")
time.sleep(2)
while counter < 3:
    counter += 1
    time.sleep(1)
    if counter == 3:
        print("------------------------ \n \nULTIMA OPORTUNDIDAD \nPISTA: Numero de sheldon en the big bang theory \n \n------------------------ \n ")
    print(f"------------------------ \nINTENTO: {counter} \n------------------------ \n ")  
    keyboard_num = int(input("- Ingrese un numero entre 1 y 100 \n-> "))

    if keyboard_num > 100 or keyboard_num < 0:
        counter -= 1
        print("------------------------ \nEL NUMERO INGRESADO NO ES VALIDO \n------------------------ \n ")   
        time.sleep(1) 
    elif keyboard_num > NUMERO_MAGICO:
        print("------------------------ \nEL NUMERO INGRESADO ES MAYOR AL NUMERO MAGICO \n------------------------ \n ")
        time.sleep(1)
    elif keyboard_num < NUMERO_MAGICO:    
        print("------------------------ \nEL NUMERO INGRESADO ES MENOR AL NUMERO MAGICO \n------------------------ \n ")
        time.sleep(1)
    else:
         print("------------------------ \n¡¡¡ADIVINASTE EL NUMERO MAGICO!! \n------------------------ \n ")   
         flag = True 
         break

if not flag: print("------------------------ \nSIGUE INTENTADO, SERÁ EN OTRA OCASIÓN :C \n------------------------ \n ")   
time.sleep(2)
print("------------------------ \n \nGRACIAS POR JUGAR\n \n------------------------ \n ")      
         