from rich import inspect
from classe import Funcionario, Horista, Mensalista

def main():
    f1 = Horista("Paulo", 12, 200)
    f1.analisar_sal()
    

    f2 = Mensalista("amanda", 9500)
    f2.analisar_sal()


if __name__ == "__main__":
    main()