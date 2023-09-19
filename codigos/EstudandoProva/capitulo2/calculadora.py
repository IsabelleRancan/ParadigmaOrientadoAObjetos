from math_operations import Operacoes

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
        somando = Operacoes.somando()

tentando = Calculadora(2,10)
print(tentando.somando())