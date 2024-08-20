pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# Elimina el ultimo elemento y lo guarda en una variable
ultimoElemento = pila.pop()

print(ultimoElemento)
print(pila)
print(pila[-1])

pila.pop()
pila.pop()


if not pila:
    print("La pila esta vacia")