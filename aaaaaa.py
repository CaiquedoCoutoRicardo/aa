class Caneta:
   def __init__(self, cor):
        self.dono = None
        self.cor = cor 

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.caneta = None

    def pegar_caneta(self, caneta):
        self.caneta = caneta
        caneta.dono = self.nome

pessoa1 = Pessoa("Caique")
caneta1 = Caneta("azul")

pessoa1.pegar_caneta(caneta1)
print(caneta1.dono)
