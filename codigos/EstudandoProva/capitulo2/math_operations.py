class Operacoes:
    "Possui as 4 operações matemáticas e a variável global pi=3.14"
    pi = 3.14

    def somando(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self, multi=0):
        return self.a * self.b
    
    def divisao(self, divisao=0):
        if self.b!=0: 
            return self.a / self.b