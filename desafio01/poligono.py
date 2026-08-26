from rich import print,inspect
from abc import ABC,abstractmethod

class Poligono(ABC):
    def __init__(self,qnt_lados):
        self.qnt_lados = qnt_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod    
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado, qnt_lados = 4):
        super().__init__( qnt_lados )
        self.lado = lado

    def perimetro(self):
        perimetro = self.lado * self.qnt_lados
        return f" O perimetro de {self.lado} e {perimetro} "
    def area(self):
        areaquadrado = self.lado ** 2
        return f" A area de {self.lado} e {areaquadrado}"
       

import math

class Circulo(Poligono):
    def __init__(self, raio, qnt_lados = 0):
        super().__init__(qnt_lados)
        self.raio = raio

    def perimetro(self):
        tpm = (2 * math.pi )*self.raio
        return f"O perimetro e {tpm:,.2f}"

    def area(self):
        area = math.pi * (self.raio **2)
        return f"A Area e {area:,.2f}"





