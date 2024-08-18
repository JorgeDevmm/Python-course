numeros = [2,4,1,45,75,22]

# numeros.sort()

# def bubble_sort():
#     temporal = ""
#     for i in range(len(numeros)-1):
#         for j in range(len(numeros)-1-i):
#             if numeros[j]>numeros[j+1]:
#                 temporal = numeros[j]
#                 numeros[j] = numeros[j+1]
#                 numeros[j+1]=temporal

# bubble_sort()

# ordenar de forma reversa con el método sort()
numeros.sort(reverse=True)
numeros.sort()

help(sort)


print(numeros)