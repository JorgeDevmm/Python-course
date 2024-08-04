""" 09_calculadora """

print("Bienvenido a la calculadora")

def ingresar_numeros():
    numero1 = int(input("Ingresar el primer numero: "))
    numero2 = int(input("Ingrear el segundo numero: "))

    return numero1,numero2


def ingresar_datos():
    resultado = 0
    numero = 0
    operador = ""

    try:
        while numero<1 or numero>4:
            print("===============================================")
            numero = int(input("Ingresar la operación a realizar [1 = suma],[2 = resta],[3 = multiplicación],[4 = División]:"))


            if numero == 1:
                operador = "Suma"
                numero1, numero2 = ingresar_numeros()
                resultado = numero1 + numero2
            elif numero == 2:
                operador = "Resta"
                numero1, numero2 = ingresar_numeros()
                resultado = numero1 - numero2
            elif numero == 3:
                operador = "Multiplicación"
                numero1, numero2 = ingresar_numeros()
                resultado = numero1 * numero2
            elif numero == 4:
                operador = "División"
                numero1, numero2 = ingresar_numeros()
                resultado = numero1 / numero2
            else:
                print("Ingresar una opción valida")

            if numero>0 and numero<5:
             print(f"El resultado de la {operador}: {resultado}")

             print("=============================================")
             operacion = input("desea continuar con otra operación: ")

             if operacion == "SI" or operacion == "Si" or operacion == "si" or operacion == "sI":
                 numero = 0
             else:
                 print("============finalizado==========")
    except ValueError:
        print("Error el valor esta vacio")



ingresar_datos()



