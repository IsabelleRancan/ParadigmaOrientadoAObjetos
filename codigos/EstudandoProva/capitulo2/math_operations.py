class Operacoes:
    "Possui as 4 operações matemáticas e a variável global pi=3.14"
    pi = 3.14

    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def somando(self, soma=0):
        soma = self.a + self.b
        return soma
    
    def subtracao(self, subtracao=0):
        subtracao = self.a - self.b
        return subtracao
    
    def multiplicacao(self, multi=0):
        multi = self.a * self.b
        return multi
    
    def divisao(self, divisao=0):
        divisao = self.a / self.b
        return divisao
        
tentativa = Operacoes(10,5)
print(tentativa.somando())
print(tentativa.subtracao())
print(tentativa.multiplicacao())
print(tentativa.divisao())
print(Operacoes.pi)