class Marca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre