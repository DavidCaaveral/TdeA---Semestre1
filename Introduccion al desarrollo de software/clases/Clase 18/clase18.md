# Clase 18 - Programación Modular

Dividir programa en sub programas abordando problemas por separado y de manera estructurada.
Para saber como dividir los problemas se utiliza el pensamiento computacional con la parte de  `abstracción` que indica la división de los problemas en subprocesos.

> **Nota:** ADICIONAL EN EL ANALISIS SE DEBE INCLUIR LA DIVISION DE PROBLEMAS EN PASOS LOGICOS

## Funciones en Python 

En **Python**, una **función** es un bloque de código reutilizable que hace una tarea específica. Se crea con `def`.

## 1. Función básica

```python
def saludar():
    print("Hola")
```

### Llamarla (ejecutarla)

```python
saludar()
```

### Resultado

```python
Hola
```

---

## 2. Función con parámetros

Los **parámetros** son datos que recibe la función.

```python
def saludar(nombre):
    print("Hola", nombre)
```

### Uso

```python
saludar("David")
```

### Resultado

```python
Hola David
```

---

## 3. Función que retorna un valor (`return`)

`return` sirve para devolver un resultado.

```python
def sumar(a, b):
    return a + b
```

### Uso

```python
resultado = sumar(5, 3)
print(resultado)
```

### Resultado

```python
8
```

---

## 4. Parámetro con valor por defecto

Si no envías el dato, usa el valor predeterminado.

```python
def saludar(nombre="Invitado"):
    print("Hola", nombre)
```

### Uso

```python
saludar()
saludar("David")
```

### Resultado

```python
Hola Invitado
Hola David
```


### Ejercicios

Elabora un **pseudocódigo** modular que calcule el valor a pagar de un empleado y las deducciones teniendo en cuenta las horas laboradas, el valor de la hora y el total de las deducciones.

- Elabora el análisis
- Construye el pseudocódigo 
- Utilizar camell-case

**Solución:**

### Analisis

**Datos de entrada:**
- valorHora: variable de tipo real
- horasTrabajadas: variable de tipo entero
- totalDeducciones: variable de tipo real
**Proceso:**
- Se definen las variables:
	- valorHora = 0
	- horasTrabajadas = 0
	- totalDeducciones = 0 
- Se harán las siguientes funciones: 
	Función salarioBruto que recibirá como parámetros las variables: valorHora y horasTrabajadas este devolverá un valor de tipo Real y hará el siguiente proceso:
		valorHora * horasTrabajadas y se retorna el resultado

	Función salarioTotal que recibirá como parámetros las variables: salarioBruto y totalDeducciones este devolverá un valor de tipo Real y hará el siguiente proceso:
		salarioBruto - totalDeducciones y se retorna el resultado

	Función Main en esta se ejecutaran las funciones anteriores y se planteara la interfaz, adicional esta no retornara nada y se leerán las siguientes variables:
	- valorHora
	- horasTrabajadas
	- totalDeducciones
	
**Datos de Salida:**
- totalDeducciones
- salarioTotal

### Pseudocódigo

Inicio

Entero horasTrabajadas
Real valorHora, totalDeducciones, varSalarioBruto

horasTrabajadas = 0
valorHora = 0
totalDeducciones = 0
 varSalarioBruto = 0
 
Función salarioBruto (real: valorHora, entero: horasTrabajadas ): Real
	retorne valorHora * horasTrabajadas
Fin Función
Función salarioTotal (real: salarioBruto , real: totalDeducciones ): Real
	retorne salarioBruto - totalDeducciones
Fin Función

Función Main(): Vacio
	Muestre "Ingrese el salario por hora del empleado"
	Leer valorHora
	Muestre  "Ingrese las horas que el empleado trabajó"
	Leer horasTrabajadas
	Muestre "Ingrese las deducciones"
	Leer totalDeducciones
	varSalarioBruto = salarioBruto(valorHora, horasTrabajadas)
	Muestre "El total del salario es: " + salarioTotal(varSalarioBruto, totalDeducciones )
	Muestre "Las deducciones aplicadas equivalen a: " + totalDeducciones

Main()

Fin
