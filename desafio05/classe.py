'''simule o sistema de batalha entre personagens de um rpg
Personagem(abc) / nome, vida, golpes / 
atavar(alvo, forca)
receber dano()
curar(abc)
Guerreiro / curar()
mago / curar())'''
from abc import ABC, abstractmethod
import random
class Personagem(ABC):
    def receber_dano(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes= []

    def atacar(self, alvo, forca=50):
        if self.vida > 0 and alvo.vida >0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print((f"{self.nome} {self.vida} atacou {alvo.nome} {alvo.vida} com um {golpe} de forca {forca}"))
            alvo.receber_dano(forca)
        else:
            print(f"O ataque{self.nome} -> {alvo.nome} nao pode acontecer")



    def receber_dano(self, dano):
        fator = random.randint(0,dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu um dano de {fator}")



    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de machado", "Pulo Giratorio"]

    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator
        print(f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {fator} pontos de vida")
    


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["bola de fogo", "raio de luz", "fogo congelante"]

    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator
        print(f"{self.nome} fez uma magia de cura e recuperou {fator} pintos de vida")
