class Perro:

    # constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    # método get
    def get_nombre(self):
        return self.__nombre
    
    # método set
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # método 
    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    # Aplicando factory method
    @classmethod
    def factory(cls):
        return cls("CHANCHO", 4)

# Acceder desde la clase a propiedad privadas
perro1 = Perro.factory()
perro1.habla()

# No se puede acceder la propiedad privada desde fuera de la clase
# print(perro1.__nombre)

# modificar una propiedad privada por medio de un metodo set
perro1.set_nombre("ROKO")

# podemos acceder por medio de un método
print(perro1.get_nombre())

# forma para acceder, No recomendable a la propiedad privada perro1.__dict__ dict contiene todas las propiedades de la instancia
print(perro1._Perro__nombre)


