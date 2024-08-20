# Diccionario las llaves son claves valor, la clave debe ser en String

punto = {"x":25,"y":50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)


if "lala" in punto:
    print(f"Encontre lala, {punto["lala"]}")
else:
    print("No encontre la llave")


# Método para traer el valor de la key del diccionario
print(punto.get("y"))

# Método para trar el valor con key no encontrada
print(punto.get("lala",97))

# Eliminar un valor x medio de su key
del punto["x"]

# Eliminar x medio de una función
del(punto["y"])

print(punto)

punto["x"] = 25

# recorrer un diccionario

for valor in punto:
    print(valor, punto[valor])

# recorrer un diccionario x medio de items - mostrara una tupla
for valor in punto.items():
    print(valor)


# Recorrer un diccionario x medio de items y desempaquetando las tuplas formadas
for key, valor in punto.items():
    print(key,valor)


# Recorrer un diccionario de listado
usuarios = [{"id": 1, "nombre": "Luis"},
            {"id": 2, "nombre": "Jorge"},
            {"id": 3, "nombre": "Maria"},
            {"id": 4, "nombre": "Adriana"}
            
]

# accedemos a la lista y luego al diccionario, posiciónandonos en el key nombre
for usuario in usuarios:
    print(usuario["nombre"])