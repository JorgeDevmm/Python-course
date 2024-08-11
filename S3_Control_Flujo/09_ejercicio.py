# calcula interactiva


def pedido_numero(operador):

    if operador == "suma":   
        resultado = numero + siguiente_numero
    if operador == "resta":
        resultado = numero - siguiente_numero
    if operador == "multi":
        resultado = numero * siguiente_numero
    if operador == "div":
        resultado = numero / siguiente_numero
    return resultado    

    


presentacion = """Bienvenidos a la calculadora 
para salir escribe salir
Las operaciones son suma, resta, multi, div"""

print(presentacion)

operacion = ""
resultado = 0
numero = 0


try:
    while operacion != "salir":

        if numero == 0:
            numero = int(input("Ingresa número: "))

        operacion = input("Ingresa Operación: ").lower()

        if operacion != "salir":
            siguiente_numero = int(input("Ingresa siguiente número: "))
        
        
        if operacion == "suma":
            print("El resultado es ",pedido_numero(operacion))
            numero = pedido_numero(operacion)
        elif operacion == "resta":
            print("El resultado es ",pedido_numero(operacion))
            numero = pedido_numero(operacion)
        elif operacion == "multi":
            print("El resultado es ",pedido_numero(operacion))
            numero = pedido_numero(operacion)
        elif operacion == "div":
            print("El resultado es ",pedido_numero(operacion))
            numero = pedido_numero(operacion)
        else:

            if operacion == "salir":
                print("========Finalizado=======")
            else:
                print("Operación no válida")
except:
    print("Valor ingresados no válido")                


   

 
     









