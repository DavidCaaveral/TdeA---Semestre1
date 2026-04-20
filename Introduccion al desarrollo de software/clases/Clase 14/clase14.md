# Ejercicio
Ejemplo 2-Algoritmo para el SIATA. El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) encargado de monitorear las condiciones meteorológicas en tiempo real, requiere un algoritmo que calcule la temperatura promedio de las lecturas enviadas por un sensor mientras que no exceda los 30°C. En caso de que esto suceda, la lectura de temperatura debe finalizar mostrando en pantalla el total de lecturas realizadas, el promedio de las temperaturas y un mensaje indicando que se superó el límite de temperatura permitido.


**Criterios para resolver el problema.**

- 1) Utilizar la constante temperatura_maxima en la solución del problema

- 2) Elaborar el análisis del problema: datos de entrada, proceso y datos de salida

- 3) Representar la solución del problema en un diagrama de flujo.

- 4) Representar la solución del problema en un pseudocódigo.

### Datos de Entrada, Proceso y Salida

**Datos de Entrada**

- temperatura_actual: dato de tipo real

**Proceso**

- Se definen las variables, temperatura_actual, TEMPERATURA_MAXIMA, Contador_temperaturas, Acumulador_temperaturas.

- Se hará un ciclo mientras con la siguiente condición “( temperatura_actual <= TEMPERATURA_MAXIMA )” dentro del ciclo se leerá la variable temperatura_actual y se harán las siguientes formulas:

	- Contador_temperaturas = Contador_temperaturas + 1
    - Acumulador_temperaturas = Acumulador_temperaturas + temperatura_actual

- Fuera del ciclo se hará la siguiente formula:

    - Promedio_temperaturas =  Acumulador_temperaturas / Contador_temperaturas

- Fuera del ciclo se definirá la variable Mensaje 
        
**Datos de Salida**

- Promedio_temperaturas
- Contador_temperaturas
- Mensaje

### Diagrama de Flujo

![img](../../imgs/diagrama%20flujo.png)

### Script

[Script.py](./script.py)