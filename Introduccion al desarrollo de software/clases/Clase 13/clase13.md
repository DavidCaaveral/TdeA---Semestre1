# Clase 13

# Ciclo while 

**Ejemplo:**

Ciclo `While`

El ciclo `while` es una estructura de control en programación que repite un bloque de código mientras una condición sea verdadera. Antes de cada iteración, evalúa la condición; si es `true`, ejecuta el código dentro del ciclo, y si es `false`, termina la ejecución.

```python
numero = 0

while numero < 6:
    print(numero)
    numero += 1

	# aquí se repite hasta que "numero" deje de cumplir una condicion en este caso es que sea menor que 6 por lo tanto el numero final es 5
```

El while puede repetirce con ayuda de booleanos y de variables de rompimiento como `break` 

```python

while True:
    variable_bandera = input("si quiere cerrar el ciclo ingrese una S\n").upper()
    if variable_bandera == "S": break

	# aquí se repite hasta que el usuario ingrese una s, ahí se rompe el ciclo 
```