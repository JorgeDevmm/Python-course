# for numero in range(1,5+1):
#     print(numero)


# paises = ["Noruega","Canada","Rusia","Bolivia","Francia","Perú","Brasil","Colombia"]

# for pais in paises:
#     if pais[0] == 'B':
#         print(pais)


# Función que pasando un numero muestra la tabla de multiplicar==================

# def multiplicacion(numero_ingresado):

#     print(f"Tabla de multilicar del {numero_ingresado}")
#     for numero in range(1,11):
#         print(f"{numero_ingresado} * {numero} = {numero_ingresado*numero}")



# for numeros in range(1,11):
#     multiplicacion(numeros)
#     print("=======================")


# imprime funcion de triangulos===============
# def imprimir_triangulo(cantidad):
#     for estrella in range(1,cantidad+1):
#         print("*" * estrella)

# imprimir_triangulo(10)


# aplicar serie de fibonacci=================
# lista_fibonacci = []


# def funcion_fibonacci(cantidad, lista):

#     a,b = 0,1
#     lista.append(a)
#     for numero in range (cantidad):
#         # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
#         c = a+b
#         lista.append(c)
#         a = b
#         b = c





# funcion_fibonacci(10, lista_fibonacci)
# print(*lista_fibonacci)

# busqueda de elemento==================
# lista_numeros = [7,9,3,5,2,7,8,1,4,6,5,8,9,3,2,1,3,7,6,9,5,3,4,5]

# def busqueda_elemento(numero):
#    contador = 0 
#    for valor in lista_numeros:
#         if valor == numero:
#             contador+=1
            
#    return contador

# numero = 9


# print(f"La cantidad de elementos del {numero} es : {busqueda_elemento(numero)} ") 


# ordenamiento burbuja ====================
# lista = [4,8,3,10,2,1,6,7,5,9]
# print(*lista)

# def ordenamiento_burbuja():
#     temporal = 0

#     for i in range(len(lista)-1):
#         for j in range(len(lista)-1 -i):
#             if lista[j]> lista[j+1]:
#                 temporal = lista[j]
#                 lista[j] = lista[j+1]
#                 lista[j+1] = temporal


# ordenamiento_burbuja()
# print(*lista)


# buscar elemento que no se encuentran===================
# buscar = 0

# for elemento in range(5):# excluyente el ultimo número
#     if elemento == buscar:
#         print("Elemento encontrado",buscar)
#         break
# else:
#     print("Elemento no encontrado")


# iterarables, range(5), listas, tuplas, string ==================

for letra in "BIENVENIDO":
    print(letra)
