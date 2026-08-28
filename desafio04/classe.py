'''crie a estrutura capaz de calcular salarios de funcionarios diferentes
Funcionario(abs)/ nome / sal_bruto / salario / sal_min = 1612/ inss = 7.5 
calc_sal(abs) / analisar_sal()
HORISTA / VALOR_HORA / HORAS_TRAB / calc_sal()
mensalista / calc_sal()'''

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self,nome , sal_bruto = 0,salario = 0,sal_min = 1620, inss = 7.5):
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss
        self.nome = nome
    
      
    def analisar_sal(self):
        self.calc_sal()


    @abstractmethod
    def calc_sal(self):
        pass

class Horista(Funcionario):
    def __init__ (self, nome, valor_hora, hora_trab, sal_min= 1612, inss = 7.5, salario = 0):
        super().__init__(nome= nome, salario=salario, sal_min=sal_min, inss=inss)
        self.valor_hora = valor_hora
        self.hora_trab = hora_trab
  

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.hora_trab 
        self.salario = (self.sal_bruto) - (self.sal_bruto / 100 * self.inss)
        calc = self.salario / self.sal_min
        print(Panel( f" O Salario de [blue]{self.nome}[/]  foi de [green]R${self.salario:,.2f}[/] que corresponde a [yellow]{calc:,.1f} salarios minimos[/]", title= "Analise de Salario", width=50))


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto=0, sal_min=1612, salario=0, inss=7.5):
        super(). __init__(nome=nome, sal_bruto=sal_bruto, sal_min=sal_min, inss=inss)

    def calc_sal(self):
        self.sal_bruto = self.sal_bruto
        self.salario = self.sal_bruto - (self.sal_bruto/100 * self.inss)
        calc = self.salario / self.sal_min
        print(Panel(f"O salario de {self.nome} e de {self.salario:,.2f} que corresponde a {calc:,.1f}.", title= "Analise de salario", width=50))