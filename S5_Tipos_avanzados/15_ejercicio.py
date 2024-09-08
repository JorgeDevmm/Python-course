from pprint import pprint

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

frase = "Bievenidos al curso de python"
caracteres_restantes = []

def quitar_espacios():
    for caracter in frase:
        if caracter != " ":
            caracteres_restantes.append(caracter)


caracteres_sin_espacios = quitar_espacios()

# print(caracteres_restantes)

# 2. Contar en un diccionario cuanto se repiten los caracteres de un string

frase2 = "lollapalooza"

def cuenta_caracteres(lista):
    total_caracteres = {}
    for caracter in lista:
        if caracter in total_caracteres:
            total_caracteres[caracter] +=1
        else:
            total_caracteres[caracter] = 1
    return total_caracteres           


total_caracteres = cuenta_caracteres(frase2)
# pprint(total_caracteres, width=1)


# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas [("a",3)]


def ordena(dict):
    return sorted(dict.items(),key=lambda key:key[1],reverse=True)

ordenados = ordena(total_caracteres)
print(ordenados)


# de un listado de tuplas, devolver las tuplas que tengan el mayor valor.
# [("a",3),("b",2),("c",4)]->[("c",4)]

print("=======================================")

def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}

    for orden in lista:
        if maximo >orden[1]:
            break
        respuesta[orden[0]]= orden[1]
    return respuesta    

mayores = mayores_tuplas(ordenados)       
print(mayores)

# Crear caracteres que más se repiten con 4 repeticiones son:
# - c
# - D

def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key,valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticion \n"
    return mensaje

caracteres_repiten = crea_mensaje(mayores)
print(caracteres_repiten)

