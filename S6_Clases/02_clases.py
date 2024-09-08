class Perro:
    # métodos funciones que se encuentran en una clase
    def habla(self, nombre):
        print(f"Guau! ladra {nombre}")

labrador = Perro()
labrador.habla("Bernardo")


print(isinstance(labrador,Perro))