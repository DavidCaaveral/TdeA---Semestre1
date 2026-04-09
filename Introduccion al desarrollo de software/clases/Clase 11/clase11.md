# clase 10

## Ciclos

### Ciclos determinados
Un ciclo determinado se define como uno al que se le define un numero de iteraciones finitas y un rango de recorrido 

**Ejemplo:**

Ciclo `for`

```python
for i in range(11):
    print(i)

# esto muestra los numeros del 1 al 10
```
>> **NOTA:** El ciclo `while` también puede ser determinado si se le coloca en la condición.

> Script: [Script](./script.py)

### Ciclos indeterminados
Un ciclo indeterminado es uno al que no se conoce cuando tendrá fin, por lo tanto se debe colocar una condición que regule las iteraciones.

> **Iteraciones:** una iteración se refiere a repeticiones.

**Ejemplo:**

Ciclo `While`

```python
numero = 0

while numero < 5:
    print(numero)
    numero += 1

	# aquí se repite hasta que "numero" deje de cumplir una condicion en este caso es que sea menor que 5 por lo tanto el numero final es 4
```
> Script2: [Script2](./script2.py)

