'''crie classes capazes de calcular frees de veiclos diferentes.
transporte (abc) / distancia / frete / cal_frete(abc)
MOTO/ FATOR = 0.50/CAL_FRETE(ABC) free
CAMINHAO / FATOR = 1.2 / CAL 50> ok
DRONE / FATOR = 9,5 / CALC FRETE 10max
'''

from abc import ABC, abstractmethod
class Transporte(ABC):
    def __init__ (self, distancia):
        self.distancia = distancia
       
    @abstractmethod
    def cal_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
    
    def cal_frete(self):
        frete = self.distancia *0.5
        return frete


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
    
    def cal_frete(self):
        if self.distancia > 50: 
            frete = self.distancia *1.2
            return frete
        else:
            return "Nao e possivel entregar nesta distancia"

class Drone(Transporte):
    def __init__(self, distancia):
            super().__init__(distancia)
        
    def cal_frete(self):
        if self.distancia > 10:
            return "Nao e possivel entregar nesta distancia"
        else:
            frete = self.distancia * 9.5
            return frete
