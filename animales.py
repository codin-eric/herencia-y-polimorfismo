class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre}")

class Perro(Mascota):
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y soy un perro")

class Gato(Mascota):
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y soy un gato")

class Pajaro(Mascota):
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y soy un pajaro")



if __name__ == '__main__':
    p1 = Perro("Framir")
    g1 = Gato("Keo")
    b1 = Pajaro("Jorge")

    p1.saludar()
    g1.saludar()
    b1.saludar()