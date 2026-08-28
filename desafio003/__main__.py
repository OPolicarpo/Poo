'''crie classes capazes de calcular frees de veiclos diferentes.
transporte (abc) / distancia / frete / cal_frete(abc)
MOTO/ FATOR = 0.50/CAL_FRETE(ABC)
CAMINHAO / FATOR = 1.2 / CAL
DRONE / FATOR = 9,5 / CALC FRETE'''
from classe import Transporte, Moto, Caminhao, Drone
def main():
    distancia = 80

    entrega = Caminhao(distancia)
    print(f"Frete de {type(entrega).__name__} em {distancia}km = {entrega.cal_frete()}")


if __name__ == "__main__":
    main()