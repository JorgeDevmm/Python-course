class Perro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # métodos funciones que se encuentran en una clase
    def habla(self):
        print(f"Guau! ladra {self.nombre} y tiene de edad {self.edad}")

labrador = Perro("Juanjo",4)
labrador2 = Perro("ROCO",12)
print(labrador.nombre)
print(labrador2.nombre)
labrador2.habla()
