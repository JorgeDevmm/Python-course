paises = ["Perú","Chile","Canada","Colombia","Ecuador","Argentina","Brasil","Venezuela","Bolivia","Ecuador"]


# contar cuantos elementos existen en el arreglo
print(paises.count("Ecuador"))

# Validar si existe el elemento y mostrar su posición
if "Alemania" in paises:
    print(paises.index("Alemania"))
else:
    print("No encontrado")    