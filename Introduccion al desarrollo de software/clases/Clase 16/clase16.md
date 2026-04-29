# Clase 16 - Arrays 

## Arreglos
Tipo de datos estructurado que puede alamcenar varios valores. Los valores deben ser del mismo tipo.

### Indice 
Un índice de un array es el número que indica la posición exacta de un elemento dentro de ese array. Es la forma de ubicar y acceder a cada dato, como si fuera la dirección de cada elemento en una lista ordenada.

Generalmente empieza en 0, así que el primer elemento tiene índice 0, el segundo índice 1, y así sucesivamente.

```python
 [4,3,8,17,43,71,62,60]
# 0,1,2, 3, 4, 5, 6, 7

```

Para recorrer los arreglos necesitamos variables `iteradoras` que se ubique en cada posición según el indice de la lista o array


**Ejemplo:**
Puntajes de un torneo gamer, el puntaje de 10 estudiantes que participaron en un torneo gamer, se encuentra almacenado en un arreglo unidimensional.

Elabora un pseudo codigo que calcule el promedio de los puntajes, el numero de puntajes mayores a 80 y el numero de puntajes menores a 80.

**Datos de entrada:**
- puntaje_estudiantes, variable de tipo arreglo 

**Proceso:**
- Se definen las varaibles:
    - iterador = 0, variable de tipo entero 
    - NUMERO_ESTUDIANTES = 10, variable de tipo entero 
    - contador_mayores = 0, variable de tipo entero 
    - contador_menores = 0, variable de tipo entero 
    - acumulador_puntajes = 0, variable de tipo real 

- se hará un ciclo de tipo **para** que tenga la condicion "(iterador <= NUMERO_ESTUDIANTES )", en el ciclo se hara la siguiente formula:

- acumulador_puntajes = acumulador_puntajes + valor de la posición actual del arreglo

- si el valor de la posición actual del arreglo es mayor o igual a 80 se hará la  siguiente formula:

    - contador_mayores = contador_mayores + 1

- si el valor de la posición actual del arreglo es menor a 80 se hará la  siguiente formula:

    - contador_menores = contador_menores + 1

- al cerrarse el ciclo se hará la siguiente formula:

    - promedio = acumulador_puntajes / NUMERO_ESTUDIANTES

**Datos de salida:**
- promedio
- contador_menores
- contador_mayores

## Pseudo codigo 
``` 
Inicio

// Declaración de las variables:

Entero puntajes_jugadores [10], variable_iteradora, suma_puntajes, promedio_puntajes, contador_menores, contador_mayores 
puntajes_jugadores [120,93,70,45,99,86,83,100,80,85]

// Inicialización de las variables:

promedio_puntajes = 0 
contador_mayores = 0
contador_menores = 0 
suma_puntajes = 0

// Proceso
Para(variable_iteradora = 0, variable_iteradora < 10, 1) hacer:
    suma_puntajes = suma_puntajes + puntajes_jugadores[variable_iteradora]

    Si (puntajes_jugadores[variable_iteradora] >= 80)
        contador_mayores = contador_mayores + 1
    SiNo
        contador_menores = contador_menores + 1
    FinSi
FinPara

promedio_puntajes = suma_puntajes / 10 

Escribir "El promedio es: ", promedio_puntajes
Escribir "el numero de puntajes mayores o iguales a 80: ", contador_mayores
Escribir "el numero de puntajes menores a 80: ", contador_menores 

Fin

```

###  Ejercicio

Likes en redes sociales:

Un estudiante quiere analizar el rendimiento de sus últimas 5 publicaciones de Instagram. Para ello registro la cantidad de likes de cada publicación en un vector. Elabora un pseudocódigo que:

- Calculé el total de likes para las 5 publicaciones 

- Calculé el promedio de likes para las 5 publicaciones 

- Muestre el total de publicaciones que tuvieron 100 o más likes 


Valores del vector

93, 56, 82, 103, 22

```
Inicio

// Declaración de las variables:

Entero likes [5], variable_iteradora, suma_likes, promedio_likes, contador_cien,
likes [93, 56, 82, 103, 22]

// Inicialización de las variables:

promedio_likes = 0 
contador_cien = 0
suma_likes = 0

// Proceso
Para(variable_iteradora = 0, variable_iteradora < 5, 1) hacer:
    suma_likes = suma_likes + likes[variable_iteradora]

    Si (likes[variable_iteradora] >= 100)
        contador_cien = contador_cien + 1
    FinSi
FinPara

promedio_likes= suma_likes / 5

Escribir "El promedio es: ", promedio_likes
Escribir "El total de likes es: ", suma_likes
Escribir "el numero de publicaciones con 100 likes en adelante: ", contador_cien

Fin

```





