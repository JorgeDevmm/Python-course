class Perro:

    def __init__(self, nombre):
        self.nombre = nombre

    # solo con la funciones que nos devuelven un valor get
    @property
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre        

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():    
           self.__nombre = nombre
        return
    


perro1 = Perro("Choclo")        
print(perro1.nombre)