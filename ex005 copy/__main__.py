from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario
from abc import ABC
def main():
    a1= Aluno("Jose", 17, "Informatica", "T01")
    a1.fazer_aniversario()
   # inspect(a1, methods= True)

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Claudia", 27, "Secretaria", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
   # inspect(f1, methods= True) 

    #x = Pessoa("Policarpo", 34)
    #x.fazer_aniversario()
    #inspect(x, methods= True)

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__=="__main__":
    main()
