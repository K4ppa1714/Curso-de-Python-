# Actividad pandas

```python
import pandas as pd

datos = {"Producto":["Mouse","Teclado","Monitor","Laptop"],
"Precio":[250,450,3200,15000],
"Existencia":[20,15,8,5]}

df = pd.DataFrame(datos)
print(df)

# la columna precio
print(df["Precio"])

# los que cuestan mas de 500
print(df[df["Precio"]>500])

df["IVA"] = df["Precio"]*0.16
df["Precio Final"] = df["Precio"] + df["Precio"]*0.16

print(df)

# menos de 10 en existencia
print(df[df["Existencia"]<10])
```

Salida:

```
  Producto  Precio  Existencia
0    Mouse     250          20
1  Teclado     450          15
2  Monitor    3200           8
3   Laptop   15000           5
0      250
1      450
2     3200
3    15000
Name: Precio, dtype: int64
  Producto  Precio  Existencia
2  Monitor    3200           8
3   Laptop   15000           5
  Producto  Precio  Existencia     IVA  Precio Final
0    Mouse     250          20    40.0         290.0
1  Teclado     450          15    72.0         522.0
2  Monitor    3200           8   512.0        3712.0
3   Laptop   15000           5  2400.0       17400.0
  Producto  Precio  Existencia     IVA  Precio Final
2  Monitor    3200           8   512.0        3712.0
3   Laptop   15000           5  2400.0       17400.0
```
