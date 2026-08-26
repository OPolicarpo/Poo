from rich import print, inspect
from classes import Aluno, Professor, Funcionario

a1= Aluno("Jose", 17, "Informatica", "T01")
a1.fazer_aniversario()
inspect(a1, methods= True)

p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario("Claudia", 27, "Secretaria", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods= True)