numeros = [2,4,1,45,75,22]

# ordenar con método sort ===========
# numeros.sort()

# ordernar con métdo de burbuja en una función ==========

# def bubble_sort():
#     temporal = ""
#     for i in range(len(numeros)-1):
#         for j in range(len(numeros)-1-i):
#             if numeros[j]>numeros[j+1]:
#                 temporal = numeros[j]
#                 numeros[j] = numeros[j+1]
#                 numeros[j+1]=temporal

# bubble_sort()

# ordenar de forma reversa con el método sort() ==========
# numeros.sort(reverse=True)

# devolver una nueva lista ordenada ascendente ==========
nueva_lista = sorted(numeros)

# devolver una nueva lista ordenada de forma descendente =========
nueva_lista_desc = sorted(numeros, reverse=True)


print(nueva_lista)
print(numeros)
print(nueva_lista_desc)


usuarios = [[4,"Jorge"],[1,"Luis"],[5,"Maria"],[2,"Angela"],[6,"Tahina"],[3,"Gabriela"]]

# si tiene una especie de dic y los numero a ordenar esta como valor, usamos una función o se ordenaran de forma alfabetica
usuarios2 = [["Jorge",4],["Luis",1],["Maria",5],["Angela",2],["Tahina",6],["Gabriela",3]]

def ordenar(usuarios2):
    return usuarios2[1]

usuarios.sort()

# ordenamiento por una key especifica que pasamos en una función y a la inversa
usuarios2.sort(key=ordenar, reverse=True)
print(usuarios)
print(usuarios2)