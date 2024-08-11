def largo(texto):
    resultado = 0
    for _ in texto:
        resultado+=1
    return resultado


print("debug")
cantidad = largo("Hola Mundo")
print(cantidad)