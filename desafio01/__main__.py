'''implemente ao seguinte diagrama de classes:
Poligono {abstract}
+ qnt lados
perimeto() {abs}
area() abt
- subs 
quadrado / lado / perimetro / area
circulo / raoo / perimetro / area
fazer uma relacao de heranca'''

from rich import print,inspect
from poligono import Poligono, Quadrado, Circulo
def main():
    a1 = Quadrado(5)
    print(a1.perimetro())
    print(a1.area())

   

if __name__ == "__main__":
    main()



