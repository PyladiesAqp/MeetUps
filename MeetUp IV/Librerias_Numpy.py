
#importar numpy
import numpy as np

#primer array usando la funcion de np.zeros
zero_vector = np.zeros(5)

#matriz bidimensional , 5 filas y 3 columnas
zero_matrix = np.zeros((5,3))

print(zero_vector)
print(zero_matrix)

# existe la funcion np.ones, identico a la sintaxis
# ..........

# matriz vacia, crea con la basura de la maemoria en donde se ha creado la matriz
empty_vector = np.empty(5)
print(empty_vector)

# matrices usando valores especificos
# variables en minuscula son vectores o matrices unidimensionales

x = np.array([1,2,3])
y = np.array([2,4,6])

print(x)
print(y)

# crear una matriz
# se especifica los elementos por fila
# entonces aqui se tiene 2 filas o dos listas
X = [[1,3],[5,9]]
print(X)

#con numpy
Y = np.array([[1,3],[5,9]])
print(Y)

# transponer una matriz
# X.trans  no se puede
transpuesta = Y.transpose()
print(transpuesta)

##########  SLICING NUMPY ARRAYS
print("SLICING NUMPY AARAYS")

x = np.array([1,2,3])
y = np.array([2,4,6])

X = np.array([[1,2,3], [4,5,6]])
Y = np.array([[2,4,6], [8,10,12]])

#acceder a un solo elemento del array
print (x[2])

#cortar un arrays

#imprime desde el primer indice hasta antes del indice indicado
print(x[0:2])

#suma de dos numpy arrays, siempre y cuando sean del mismo tamaño
z = x + y
print(z)

# bidimensionales acceso
# tiene acceso a la columna 1
print(X[:,1])
print(Y[:,1])

# suma de columnas especificas de una matriz
Z = X[:,1] + Y[:,1]
print(Z)

# tiene acceso a la primera fila
print(X[1,:])

#suma de filas especificas de una matriz
W = X[1,:] + Y[1,:]
print(W)

# tambien se puede obtener la fila en una posicion
print(X[1])

# Advertencia, si queremos sumar los arrays como anteriormente se quiso hacer,
#lo que hace concatenar

print([2,4] + [6,8])

# En cambio si se utiliza la libreria numpy, suma los elementos

var = np.array([2,4]) + np.array([6,8])
print(var)

# prueba // sumar estos dos arreglos

a = np.array([1,2])
b = np.array([3,4,5])