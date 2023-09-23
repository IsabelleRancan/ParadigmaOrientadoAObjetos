from math_operations import Operacoes 

class Retangulo: 
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def area_retangulo(self):
        resultado = Operacoes.multiplicacao(self)
        return resultado

class Circulo: 
    def __init__(self, b):
        self.b = b
        self.a = Operacoes.pi

    def area_circulo(self):
        self.b = Operacoes.raiz(self)
        resultado = Operacoes.multiplicacao(self)
        return resultado

class Triangulo: 
    def __init__(self, b, a, ):
        self.b = b
        self.a = a

    def area_triangulo(self):
        """Usando os métodos para fazer as operações
        mudando os valores de a e b para poder fazer a divisão"""
        resultado = Operacoes.multiplicacao(self)
        self.a = resultado
        self.b = 2
        resultado = Operacoes.divisao(self)
        return resultado
    
testeTri = Triangulo(7.5, 30)
print(testeTri.area_triangulo())

testeRetangulo = Retangulo(5, 10)
print(testeRetangulo.area_retangulo())

testeCirculo = Circulo(5)
print(testeCirculo.area_circulo())