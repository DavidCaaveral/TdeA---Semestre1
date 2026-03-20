## Parte 1 - Preguntas de reflexión inicial 

### 1. ¿Qué diferencia existe entre dato e información?

#### Dato:
Representación simbólica de algo sin contexto propio **Ejemplo: "5"**

#### Información:
Conjunto de datos procesados y ordenados con una utilidad  y significado

En resumen el dato por si solo no da significado pero al ser un conjunto se le da un contexto y eso es información.

---
### 2. ¿Puede existir Inteligencia Artificial sin datos?

Respuesta :  **NO**

los datos generan clusters los cuales hacen parte del **machine learning** (aprendizaje basado en datos) usado en las redes neuronales que componen una IA

---

### 3. ¿Un Excel con fórmulas es IA? ¿Por qué?

Respuesta :  **NO**

Excel no cuenta con la capacidad de memoria, el modelo de lenguaje ni el sistema de aprendizaje necesarios para tener la precisión y la capacidad de aprendizaje que se requieren.

---
## Parte 2 - Línea del Tiempo Conceptual 

> Trabajo realizado en compañía de **Samuel Ovando Lizarazo**

![alt text](image.png)

---

## Parte 3 - Análisis Crítico


### 1. ¿En qué etapa se encuentra actualmente Colombia frente a la IA? 

Actualmente Colombia se une al uso habitual, recurrente y personal de la IA siendo un material importante en ámbitos de estudio, redacción u ofimática.

> Aun en Colombia no se ha estandarizado de manera significativa el uso de IA a nivel corporativo o industrial

### 2. ¿Qué riesgos implica depender excesivamente de la IA? 

Como experiencia personal, debo reconocer que el uso excesivo de la IA produce hoy en día una falta de pensamiento crítico real. Además, puede generar información o resultados pobres y cierto tipo de ‘enfriamiento’ intelectual debido al poco uso de nuestro cerebro a causa de la dependencia de estas herramientas.

### 3. ¿Qué habilidades debe desarrollar un ingeniero de software en la era de la IA?

- Prompting: Funcionamiento de los textos ingresados a las IA
- Lectura critica: Para interpretación de resultados y entendimiento de las peticiones
- Lógica Pura: desarrollo de funcionalidades
- Comunicación asertiva: Fomentar el trabajo sano en equipo 
- Coding.

---

## Parte 4 - Aplicación Práctica (integración con Power BI) 

Se entrega un conjunto de datos simple (ventas de una tienda).

> **Nota previa:** la obtención de los datos se hace por medio de la plataforma [Kaggle](https://www.kaggle.com)

### Propósito:

Extraer datos reales que hayan sido usados en negocios, para así poder evaluar la identificación e interpretación de información  por parte del estudiante, la información presentada en este reporte de ejemplo se encuentra publica y de libre adquisición.

Extracción de datos: [ETL](./data%20activities/data.ipynb)

| sale_id | branch | city        | customer_type | gender | product_name | product_category | unit_price | quantity |  tax | total_price | reward_points |
| ------: | ------ | ----------- | ------------- | ------ | ------------ | ---------------- | ---------: | -------: | ---: | ----------: | ------------: |
|       1 | A      | New York    | Member        | Male   | Shampoo      | Personal Care    |       5.50 |        3 | 1.16 |       17.66 |             1 |
|       2 | B      | Los Angeles | Normal        | Female | Notebook     | Stationery       |       2.75 |       10 | 1.93 |       29.43 |             0 |
|       3 | A      | New York    | Member        | Female | Apple        | Fruits           |       1.20 |       15 | 1.26 |       19.26 |             1 |
|       4 | A      | Chicago     | Normal        | Male   | Detergent    | Household        |       7.80 |        5 | 2.73 |       41.73 |             0 |
|       5 | B      | Los Angeles | Member        | Female | Orange Juice | Beverages        |       3.50 |        7 | 1.72 |       26.22 |             2 |

### 1. Identificar qué es dato.

Los datos como tal son lo mas básico que aparece en la tabla antes de contextualizar y darles interpretación.

| sale_id | branch  | city         | customer_type  | gender | product_name | product_category  | unit_price | quantity |  tax | total_price | reward_points |
| ------: | ------- | ------------ | -------------- | ------ | ------------ | ----------------- | ---------: | -------: | ---: | ----------: | ------------: |
|       1 | A       | New York     | Member         | Male   | Shampoo      | Personal Care     |       5.50 |        3 | 1.16 |       17.66 |             1 |

un ejemplo de esto puede ser `Shampoo` en un principio, el string como tal no tiene ningún sentido, sin embargo si leemos su encabezado:

| Product_name |
|-----------------|

  Hasta aquí entendemos que se refiere al nombre de un producto, posteriormente a este se le dará un significado de fila, que termine en la información de una **compra**
### 2. Convertirlo en información (tabla organizada).

Si bien un dato por si solo puede representar bastante, al estructurar, organizar y limpiar **(ETL)** se obtienen conjuntos de datos organizados

| index | Id_ventas | Rama | ciudad      | Tipo_de_cliente | genero    | nombre_producto | categoria_producto | precio_unitario | cantidad | impuesto | precio_total | puntos |
| ----- | --------- | ---- | ----------- | --------------- | --------- | --------------- | ------------------ | --------------- | -------- | -------- | ------------ | ------ |
| 0     | 1         | A    | New York    | Miembro         | Masculino | Shampoo         | Cuidado personal   | 5.5             | 3        | 1.16     | 17.66        | 1      |
| 1     | 2         | B    | Los Angeles | Normal          | Femenino  | Cuaderno        | Papelería          | 2.75            | 10       | 1.93     | 29.43        | 0      |
| 2     | 3         | A    | New York    | Miembro         | Femenino  | Manzana         | Frutas             | 1.2             | 15       | 1.26     | 19.26        | 1      |
| 3     | 4         | A    | Chicago     | Normal          | Masculino | Detergente      | Hogar              | 7.8             | 5        | 2.73     | 41.73        | 0      |
| 4     | 5         | B    | Los Angeles | Miembro         | Femenino  | Jugo de naranja | Bebidas            | 3.5             | 7        | 1.72     | 26.22        | 2      |
| 5     | 6         | A    | Chicago     | Normal          | Masculino | Shampoo         | Cuidado personal   | 11.24           | 9        | 7.08     | 108.24       | 0      |
| 6     | 7         | A    | Chicago     | Normal          | Masculino | Shampoo         | Cuidado personal   | 10.71           | 1        | 0.75     | 11.46        | 0      |
| 7     | 8         | B    | Los Angeles | Normal          | Femenino  | Shampoo         | Cuidado personal   | 18.23           | 9        | 11.48    | 175.55       | 0      |
### 3. Generar conocimiento (conclusión).
para complementar este subpunto se llevara a cabo un reporte con los datos anteriormente explicados a través de Power BI con el cual se le dará un sentido corporativo y adecuado con las metodologías de **Business Intelligence**.

[Reporte](./data%20activities/Reporte%20Ejemplo.pbix)

![alt](./power%20bi.jpeg)
### 4. Proponer cómo una IA podría mejorar el proceso.

El proceso de creación y análisis de datos puede optimizarse a niveles gigantescos con ayuda de la IA ya que con esta, la creación de reportes, algoritmos, sistemas de predicción y ayudas, se ven optimizados, como sociedad debemos empezar a aceptar la sinergia con los dispositivos que inducen a una mayor capacidad de trabajo y avance.

---
### Trabajo Realizado por:

- Samuel Obando Lizarazo
- David Cañaveral Lopera 
