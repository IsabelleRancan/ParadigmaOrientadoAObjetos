class Funcoes:

    def fatorial(self, n):
        self.n = n
        
        if n == 0 or n == 1:
            return 1 
        else:
            return n * self.fatorial(n - 1)
        
    def fibonacci(self, n):
        self.n = n 
        self.vetor = [0]
        self.p1 = 0
        self.p2 = 1

        if n == 0:
            return (self.vetor)
        else:
            for elemento in self.vetor:
                self.vetor.append(self.p1 + self.p2)
                self.p1 = self.p2
                self.p2 = elemento
            return(self.vetor)
        
teste = Funcoes()
print(teste.fatorial(5))

teste2 = Funcoes()
print(teste.fibonacci(0))
        
