from abc import ABC, abstractmethod

class FormaGeometrica:

    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
retangulo=Retangulo(5, 10)
print(f"A área do retângulo é: {retangulo.calcular_area()}")