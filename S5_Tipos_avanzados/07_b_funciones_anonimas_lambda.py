# si tiene una especie de dic y los numero a ordenar esta como valor, usamos una función o se ordenaran de forma alfabetica
usuarios2 = [["Jorge",4],["Luis",1],["Maria",5],["Angela",2],["Tahina",6],["Gabriela",3]]


# ordenamiento por una key especifica que pasamos en una función y a la inversa
usuarios2.sort(key=lambda elemento:elemento[1], reverse=True)

print(usuarios2)