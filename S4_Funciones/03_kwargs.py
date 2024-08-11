# multiples argumentos como diccionario==============

def get_product(**datos_personales):
    print(datos_personales)


datos_personal = {"dni":45678121, "nombre":"Luis","apellido":"Morales"}    

# desempaquetar diccionario con sus valores
get_product(**datos_personal)


# kwargs================
# def get_product2(**datos):
#     print(datos)


# get_product2(id="id",name="iphone",desc="Esto es un iphone")


# acceder a un elemento especifico de kwargs==============
def get_product2(**datos):
    print(datos["id"],datos["name"])


get_product2(id="id",name="iphone",desc="Esto es un iphone")