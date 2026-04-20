# Ejercicio
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

- TEMPERATURA_MAXIMA = 26, variable de tipo real 
- TEMPERATURA_MINIMA = 16, variable de tipo real
- TOTAL_TEMPERATURAS = 12, variable de tipo entero
- TEMPERATURA_NORMAL = 0, variable de tipo real

**Proceso**

**Datos de Salida**