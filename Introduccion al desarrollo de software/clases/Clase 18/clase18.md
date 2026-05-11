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
