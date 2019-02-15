import numpy as np

# construir un array que contenga 10 elementos espaciados
# linealmente comenzando de 0 y terminando en 100

lin = np.linspace(0, 100, 10)
print(lin)

# construir un array que contenga 10 elementos espaciados logaritmicamente
# comenzando de 10 y terminando en 100
# logaritmo de 10 en base 10 es 1
# logaritmo de 100 en base 10 es 2

log = np.logspace(1, 2, 10)
print(log)

## otro ejemplo comenzando en 250 y terminando en 500

log1 = np.logspace(np.log10(250), np.log10(500), 10)
print(log1)

## para saber la forma de un array // bidimensional

X = np.array([[1,2,3],[4,5,6]])
print("Forma del array")
print(X.shape)

## para saber la cantidad de elementos que contiene el array
print(X.size)

#### Aveces se tiene que verificar si los elementos deban cummplir alguna condicion

# generamos un array con valores aleatorios // 10 numeros aleatorios // estandar del 0 al 1

x = np.random.random(10)
print(x)

# primera condicion si al menos un elemento sea mayor a 0.9
print(np.any(x > 0.9))

# segunda condicion, que todos sean mayres a 0.1
print(np.all(x >= 0.1))