class Perro:

    patas = 4

    # constructor
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # método propio de la clase
    @classmethod
    def habla(cls):
        print("Guau!")

    # Aplicando factory method
    @classmethod
    def factory(cls):
        return cls("CHANCHO", 4)
    

    def mostrar_informacion(self):
        print(f"El nombre es: {self.nombre} y su edad es: {self.edad}")
        


Perro.habla()

perro1 = Perro("ROCO",2)
perro1 = Perro("FIRULAIS",3)

Perro3 = Perro.factory()

Perro3.mostrar_informacion()

