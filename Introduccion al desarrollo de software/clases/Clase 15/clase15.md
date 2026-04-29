# Ejercicio - SIATA V2
Después de revisar los resultados obtenidos con la primera versión del algoritmo para monitorear en tiempo real las condiciones meteorológicas de Medellín, el SIATA te encargó el diseño de la segunda versión que debe calcular la temperatura promedio de la ciudad durante un día con las lecturas que envía el sensor cada 120 minutos, teniendo en cuenta el rango **16 °C <= temperatura <= 26 °C.** Adicionalmente, el algoritmo debe calcular el número de veces que la temperatura fue normal, inferior a 16°C y mayor que 26°C.

**Antes de resolver el algoritmo responde las siguientes preguntas:**

- ¿Cuántas temperaturas debe procesar el algoritmo? ¿Por qué?
- ¿Cuál es la estructura que debes usar para la iteración? ¿Por qué?
- ¿Qué significa la expresión 16 °C <= temperatura <= 26 °C?
- ¿Cuáles son las temperaturas que se consideran normales?


**Criterios para resolver el problema.**

1. Utilizar las constantes temperatura_maxima, temperatura_normal y total_temperaturas en la solución del problema.
2. Elaborar el análisis del problema: datos de entrada, proceso y datos de salida.
3. Representar la solución del problema en un diagrama de flujo.
4. Representar la solución del problema en un pseudocódigo.

**Respuestas:**
- **12**, Porque al tomar temperaturas cada 120 minutos sería cada 2 horas lo que hace que se tomen 12 temperaturas al dia

- **Determinado**, ya que está establecido el limite de 12 temperaturas, se deberá usar un ciclo for 

- Significa: la temperatura normal se encuentra entre 16 °C y 26 °C

- Las temperaturas que se consideran normales son las que están entre 16° y 26°

### Datos de Entrada, Proceso y Salida

**Datos de Entrada**

temperatura_actual = 0, variable de tipo real

**Proceso**
- Se definirán las siguientes variables: 
    - TEMPERATURA_MAXIMA = 26, variable de tipo real 
    - TEMPERATURA_MINIMA = 16, variable de tipo real
    - TOTAL_TEMPERATURAS = 12, variable de tipo entero
    - contador_mayor = 0
    - contador_menor = 0 
    - contador_normales = 0  
    - acumulador_general = 0

- Se hará un ciclo for que tenga la condicion de "(iterador <= TOTAL_TEMPERATURAS)" dentro del ciclo se leerá la variable temperatura_actual y se hará la siguiente
formula:

acumulador_general = acumulador_general + temperatura_actual

y luego los siguientes condicionales:

si la temperatura_actual es mayor o igual a la TEMPERATURA_MAXIMA haga esta formula:
contador_mayor = contador_mayor + 1

si la temperatura_actual es menor o igual a la TEMPERATURA_MINIMA haga esta formula: 
contador_menor = contador_menor + 1

si no es ninguna de las anteriores haga esta formula:
contador_normales = contador_normales + 1

al cerrar el ciclo se hará la siguiente formula:

promedio_temperaturas = acumulador_general / TOTAL_TEMPERATURAS


**Datos de Salida**

- contador_mayor
- contador_menor
- contador_normales
- promedio_temperaturas


### Diagrama de flujo 
![img](../../imgs/doble%20condicional.drawio.png)

### Script 
[Script.py](./script.py)

--- 
## Pensamiento Computacional

Es una forma de razonar orientada a resolver problemas de manera estructurada, usando principios de la informatica.

Se trata de aprender a analizar, problemas, descomponerlos y construir soluciones claras, logicas y escalables 

Se resume en: pensar como lo haria un sistema, paso a paso, con reglas definidas y demanera eficiente.

### Pasos del pensamiento computacional

1. **Descomposición**
    - Consiste en dividir un problema grande en partes mas pequeñas y simples, buscando facilitar el entendimiento de cada parte del problema sin abrumarse con el problema en completo

2. **Reconocimiento de patrones**
    - En este punto se indican similitudes o comportamientos repetitivos entre los problemas o sus partes 

3. **Abstracción**       
    - Este punto busca enfocarse en los aspectos importantes del problema evitando los detalles innecesarios

4. **Diseño de algoritmos**     
    - Creación de una serie de pasos ordenados y logicos para resolver el problema

### Como contribuye al desarrollo de software

El pensamiento computacional contribuye a una comprensión más clara y estructurada de un problema, lo que permite abordarlo de manera más eficiente mediante herramientas informáticas.

