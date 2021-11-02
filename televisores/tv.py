class TV:

    numTV = 0

    def __init__(self, marca, estado:bool) -> None:
        self.marca = marca
        self.estado = estado
        self.canal = self.volumen = 1
        self.precio = 500
        TV.numTV += 1


    def getMarca(self):
        return self.marca

    def getControl(self):
        return self.control

    def getPrecio(self):
        return self.precio
    
    def getVolumen(self):
        return self.volumen

    def getCanal(self):
        return self.canal

    def setMarca(self, marca):
        self.marca = marca

    def setControl(self, control):
        self.control = control

    def setPrecio(self, precio):
        self.precio = precio

    def setVolumen(self, volumen):
        if (0 <= volumen <=7) and self.estado:
            self.volumen = volumen

    def setCanal(self, canal):
        if (1 <= canal <=120) and self.estado:
             self.canal = canal

    @classmethod
    def getNumTV(cls):
        return cls.numTV

    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado and self.canal < 120:
            self.canal+=1
		
    def canalDown(self):
        if self.estado and self.canal > 1: 
            self.canal-=1
            
    def volumenUp(self): 
        if self.estado and self.volumen < 7: 
            self.volumen += 1
	
    def volumenDown(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1