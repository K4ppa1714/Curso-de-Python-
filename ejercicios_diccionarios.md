# Ejercicios de diccionarios

## 1. Registrador de estudiantes

La función solo arma el diccionario con los parámetros que recibe. La llave `activo` no viene de fuera, la pongo fija en `True` porque un estudiante que se acaba de registrar se asume activo.

```python
def crear_estudiante(nombre, edad, carrera):
    return {'nombre': nombre, 'edad': edad, 'carrera': carrera, 'activo': True}

alumno = crear_estudiante("Daniel", 21, "Computación")
print(alumno)
```

Salida:

```
{'nombre': 'Daniel', 'edad': 21, 'carrera': 'Computación', 'activo': True}
```

## 2. Consultar precios

Usé `.get()` en vez de `inventario[producto]` porque los corchetes revientan con un KeyError cuando la clave no existe, y `.get()` nada más regresa `None`. Con eso ya puedo decidir cuál de los dos mensajes devolver.

Comparo contra `None` y no con `if precio:` porque si algún producto llegara a costar 0, el `if` lo tomaría como falso y diría que no está disponible.

```python
def obtener_precio(inventario, producto):
    precio = inventario.get(producto)
    if precio is None:
        return f"El producto {producto} no está disponible"
    return f"El precio de {producto} es ${precio}"

precios = {"manzana": 15.5, "pila": 25.0, "cuaderno": 45.0}

print(obtener_precio(precios, "pila"))
print(obtener_precio(precios, "lapicero"))
```

Salida:

```
El precio de pila es $25.0
El producto lapicero no está disponible
```

## 3. Contador de frecuencia

Recorro el texto letra por letra. Si la letra ya está en el diccionario le sumo 1, y si es la primera vez que aparece la creo con valor 1.

```python
def contar_caracteres(texto):
    conteo = {}
    for letra in texto:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    return conteo

print(contar_caracteres("programacion"))
```

Salida:

```
{'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 2, 'm': 1, 'c': 1, 'i': 1, 'n': 1}
```

Se puede acortar el `if/else` a `conteo[letra] = conteo.get(letra, 0) + 1`, hace exactamente lo mismo.

## 4. Filtrado de calificaciones

Recorro con `.items()` para tener nombre y nota al mismo tiempo, y voy llenando un diccionario nuevo nada más con los que pasan. El `= 6.0` en el parámetro es el valor por defecto, así que se puede llamar la función sin mandar la nota mínima.

```python
def filtrar_aprobados(calificaciones, nota_minima=6.0):
    aprobados = {}
    for nombre, nota in calificaciones.items():
        if nota >= nota_minima:
            aprobados[nombre] = nota
    return aprobados

grupo = {"Ana": 8.5, "Carlos": 5.0, "Sofia": 9.2, "Luis": 5.8, "Diana": 7.0}
print(filtrar_aprobados(grupo, nota_minima=6.0))
```

Salida:

```
{'Ana': 8.5, 'Sofia': 9.2, 'Diana': 7.0}
```

Ojo con Luis: saca 5.8 y no entra, la comparación es `>=` contra 6.0.
