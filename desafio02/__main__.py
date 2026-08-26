''' Simule uma cafeteria orientada a objetos

BEBIDAQUENTE (ABS) / preparar () / ferver-agua()/ miturar (abs) / servir (abs)
CAFE / MISTURAR / SERVIR
CHA / MISTURAR . SERVIR. 
LEITE / MISTURAR / SERVIR '''
from cafeteria import BebidaQuente, Cafe, Leite, Cha

def main():
    bebida = Cafe()
    bebida.preparar()


if __name__ == "__main__":
    main()