# Aplicando comprensión de lista

usuarios2 = [["Jorge",4],["Luis",1],["Maria",5],["Angela",2],["Tahina",6],["Gabriela",3]]


usuarios2.sort(key=lambda elemento: elemento[1])

# sacar los valores[0] cuando la lista tiene una tupla interna
# usuarios3 = []
# for usuario in usuarios2:
#     usuarios3.append(usuario[0])

# print(usuarios3)


# tranformación de lista 
# lista  =  expresion for item in items
# usuarios3 = [usuario[0] for usuario in usuarios2]
# print(usuarios3)

# filtrar lista
# usuarios3 = [usuario for usuario in if usuario[1]]

# filtrado y transformación de lista
usuarios4 = [usuario[0] for usuario in usuarios2 if usuario[1] > 2]

print(usuarios4)
