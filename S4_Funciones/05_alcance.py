saludo = "Hola global"

def saludar():
    global saludo
    saludo = "Hola Mundo"


def saluda2():
    saludo = 24
    print(saludo)

print(saludo)
saludar()
print(saludo)    