''' Simule uma cafeteria orientada a objetos

BEBIDAQUENTE (ABS) / preparar () / ferver-agua()/ miturar (abs) / servir (abs)
CAFE / MISTURAR / SERVIR
CHA / MISTURAR . SERVIR. 
LEITE / MISTURAR / SERVIR '''
from abc import ABC, abstractmethod
class BebidaQuente(ABC):
    def __init__(self):
        pass
    
    def preparar(self):
        print("--Iniciando preparo --")
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print("1- Fervendo a agua a 100 graus celcius")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod    
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__ (self):
        super().__init__()
        
    def misturar(self):
        print("2- Passando agua pressurizada pelo po de cafe")
    
    def servir(self):
        print("3- Servindo em xicara pequena")
        print("---Bebida Pronta___")

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2- Mergulhando o sache de ervas na agua. ")
    
    def servir(self):
        print("servindo na caneca de porcelana com limao")
        print("---Bebida Pronta___")


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print("2- Passando vapor pressurizado pelo bico do leite")
    
    def servir (self):
        print("servindo na caneca grande, ja com cafe.")
        print("---Bebida Pronta___")