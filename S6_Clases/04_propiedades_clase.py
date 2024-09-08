class Perro:

    patas = 4

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # métodos funciones que se encuentran en una clase
    def habla(self):
        print(f"Guau! ladra {self.nombre} y tiene de edad {self.edad}")

labrador = Perro("Juanjo",4)
labrador2 = Perro("ROCO",12)

labrador2.patas = 5
Perro.patas = 3
print(Perro.patas)
print(labrador2.patas)



print(labrador.nombre)
print(labrador2.nombre)

labrador2.habla()
