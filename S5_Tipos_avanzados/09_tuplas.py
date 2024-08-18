# Las tuplas son inmutables pero podemos asignar una tupla a otra

numeros = (1,2,3) + (4,5,6)
print(numeros)


# convertir tupla con la función tuple, con una lista
punto = tuple([1,2])

# convertir tupla con la función tuple, con el iterable range
punto2 = tuple(range(1,11))

# convertir tupla con la función tuple, con el iterable range
punto3 = tuple("Bienvenido")

# asignamos en una nueva variable y con slicing (Segmentación)
punto4 = numeros[:2]

# Desempaquetar la tupla
primero, segundo, *otros = numeros

print(punto)
print(punto2)
print(punto3)
print(punto4)
print(primero, segundo,otros)

# Iterar tuplas 
for numero in numeros:
    print(numero, end=" ")

print()

# para iterar tupla, tenemos que convertirlo en lista
lista_nueva = list(numeros)
lista_nueva[0] = "valor cambiado"
print(lista_nueva)