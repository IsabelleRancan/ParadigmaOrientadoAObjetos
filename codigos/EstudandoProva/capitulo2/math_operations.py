class Operacoes:
    "Possui as 4 operações matemáticas e a variável global pi=3.14"
    pi = 3.14

    def somando(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b
    
    def divisao(self):
        if self.b!=0: 
            return self.a / self.b

    def raiz(self):
        return self.b ** 2