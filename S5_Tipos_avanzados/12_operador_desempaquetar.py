# desempaquetar los valores de una lista

lista = [1,2,3,4]

print(1,2,3,4)

print(*lista)

lista2 = (1,2,3,4)

print(lista2)

# Combinando dos listas

lista3 = [1,2,3,4]
lista4 = [5,6]

lista_combinada = ["hola",*lista3,"mundo",*lista4,"Bienvenido"]

print(lista_combinada)

# Aplicando en diccionarios -> la asignación es de derecha a izquierda

punto1 = {"x":19, "y": "hola"}
punto2 = {"y":19}

nuevoPunto = {**punto1,"lala": "hola mundo",**punto2,"z": "mundo"}

print(nuevoPunto)


# otra forma de desempaquetar valor por meid del modulo 

from collections import deque

# crea una lista

fila = deque([1,2])
# fila.append(3)
# fila.append(4)
# fila.append(5)
print(fila)

# método que elimina un elemento a la izquierda
fila.popleft()
fila.popleft()
print(fila)

if not fila:
    print("fila vacia")
