# for numero in range(1,5+1):
#     print(numero)


# paises = ["Noruega","Canada","Rusia","Bolivia","Francia","Perú","Brasil","Colombia"]

# for pais in paises:
#     if pais[0] == 'B':
#         print(pais)


# Función que pasando un numero muestra la tabla de multiplicar

# def multiplicacion(numero_ingresado):

#     print(f"Tabla de multilicar del {numero_ingresado}")
#     for numero in range(1,11):
#         print(f"{numero_ingresado} * {numero} = {numero_ingresado*numero}")



# for numeros in range(1,11):
#     multiplicacion(numeros)
#     print("=======================")


# imprime funcion de triangulos
# def imprimir_triangulo(cantidad):
#     for estrella in range(1,cantidad+1):
#         print("*" * estrella)

# imprimir_triangulo(10)


# aplicar serie de fibonacci
lista_fibonacci = []


def funcion_fibonacci(cantidad, lista):

    a,b = 0,1
    lista.append(a)
    for numero in range (cantidad):
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
        c = a+b
        lista.append(c)
        a = b
        b = c





funcion_fibonacci(10, lista_fibonacci)
print(*lista_fibonacci)
