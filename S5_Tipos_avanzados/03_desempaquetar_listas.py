numeros = [1,2,3]

# mala practica
# primero = numeros[0]
# primero = numeros[1]
# primero = numeros[2]

# forma correcta de desempaquetar números
primero, segundo, tercero = numeros
print(primero,segundo,tercero)

numeros = list(range(1,11))

# otra forma de solo sacar el primer elemento de una lista
primero, *otros = numeros
print(primero,otros)

primero, segundo, *otros = numeros
print(primero,segundo,otros)

primero, segundo, *otros,penultimo, ultimo = numeros
print(primero,segundo,otros,penultimo, ultimo)

