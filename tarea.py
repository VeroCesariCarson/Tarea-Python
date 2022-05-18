class Mamifero:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def caminar(self):
        print(f'{self.nombre} camina con {self.patas} patas')