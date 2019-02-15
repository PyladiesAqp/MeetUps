import numpy as np

### INDEXING

# Definir un array

z1 = np.array([1,3,5,7,9])
print("Z1:", z1, '\n')
z2 = z1 + 1
print("Z2:", z2, '\n')

# Crear una lista que me va a permitir indexar los dos arrays anteriores

ind = [0,2,3]

# ahora puedo acceder a esos 3 indices de mis arrays

print(z1[ind])

# pero si convierto mi lista ind en un numpy array, tambien puedo acceder a esos indices

ind = np.array([0,2,3])

print(z1[ind])
print(z2[ind])

# array con valores booleanos o array logica
print(z1> 6)

# acceder a los elementos del array utilizando un vector de indice logico

print(z1[z1 > 6])
print(z2[z1 > 6])

# Tambien se puede crear un vector logico
ind = z1 > 6
print(ind)
# puedo obtener el mismo resultado de la anterior operacion
print(z1[ind])
print(z2[ind])

## como cortar un array con dos puntos ---- cuidado lleva a errores

w = z1[0:3]
print(w)

# modificar un elemento en la ubicacion de cero
w[0] = 3
print(w)

## pero ojo con esto // se cambio tambien la posicion 0
print(z1)

### Pero que sucederia si utilizamos la indexacion

z1 = np.array([1,3,5,7,9])
indices = np.array([0,1,2])
print(z1)
print(indices)

# ahora voy a indexar

w = z1[indices]
print(w)

w[0] = 3
print(w)
## no ha cambiado mi array original
print(z1)


a = np.array([1,2])
b = np.array([3,4,5])
print(b[a])

c = b[1:]
print(c)
print (b[a] is c)