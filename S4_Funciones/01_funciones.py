# Funciones

# print("Hola Mundo")

# def hola():
#     print("Hola Mundo!")
#     print("Ultimate Python")


# hola()    
# hola()    
# hola()    
# hola()    

# Funciones con Argumentos
def saludo(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(F"Bienvenido {nombre} {apellido}")


saludo("Jorge","Monzón")
saludo("Personaje")

# Argumentos opcionales
def saludo(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(F"Bienvenido {nombre} {apellido}")


saludo("Jorge","Monzón")
saludo("Personaje")


# Argumentos nombrados
saludo(apellido="Morales",nombre="Luis")