# Las funciones map y fiter toman como argumentos una función lambda con un item, un retorno y el la lista a iterar, 
# en caso de filter considera si es True la condición para devolver el fitrado

usuarios2 = [["Jorge",4],["Luis",1],["Maria",5],["Angela",2],["Tahina",6],["Gabriela",3]]


# aplicando map = transformación =======
# usuarios3 = list(map(lambda usuario: usuario[0], usuarios2))


# aplicando filter =========
usuarios3 = list(filter(lambda usuario:usuario[1] > 2, usuarios2))

print(usuarios3)

