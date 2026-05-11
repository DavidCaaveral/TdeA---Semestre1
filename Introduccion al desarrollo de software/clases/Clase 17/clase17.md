# Clase 17 - Estructura de código en python

### Estándar de codificación

Es una **forma estándar de organizar código en Python** donde separas claramente importaciones, constantes, funciones, clases y el punto de ejecución (`main`), lo que hace el programa más claro, reutilizable y fácil de mantener; no cambia lo que el código hace, sino cómo está estructurado para trabajar mejor en proyectos reales.

La diferencia con la codificación por scripts es que un **script simple** suele escribirse de forma lineal (todo se ejecuta de arriba hacia abajo, sin mucha estructura), mientras que este enfoque organizado divide responsabilidades y usa `if __name__ == "__main__":` para controlar cuándo se ejecuta el programa, permitiendo reutilizar partes del código en otros archivos sin que se ejecuten automáticamente.

``` python

'''
Autor: 
Versión:
Fecha:
Descripción:
'''

# 1. Importaciones de librerías



# 2. Definición de constantes globales



# 3. Definición de funciones



# 4. Definición de clases (opcional)




# 5. Bloque principal de ejecución
def main():



# 6. Punto de entrada
if __name__ == "__main__":
    main()
    

```


### Ejercicio de clase: 

Contruye un script de python que lea 2 numeros enteros positivos y que calcule para ellos la suma la multiplicación y la división 

> **Script:** [script](./script.py)