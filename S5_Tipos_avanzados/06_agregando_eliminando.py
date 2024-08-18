paises = ["Perú","Chile","Canada","Colombia","Ecuador","Argentina","Brasil","Venezuela","Bolivia","Ecuador"]

# Agregar un elemento en una posición en especifica
paises.insert(1,"Jamaica")

# Agregar elementos al final de la lista
paises.append("China")

# Eliminar un elemento de la lista x valor
paises.remove("Ecuador")

# Eliminar elemento x posición
paises.pop(1)

del paises[0]

paises.clear()


print(paises)