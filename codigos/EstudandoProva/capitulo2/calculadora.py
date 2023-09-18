from math_operations import Operacoes

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculando(self):
        return Operacoes.somando(self), Operacoes.subtracao(self), Operacoes.multiplicacao(self), Operacoes.divisao(self)
    

tentando = Calculadora(2,10)
print(tentando.calculando())