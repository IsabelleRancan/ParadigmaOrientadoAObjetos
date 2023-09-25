class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(f'O animal {self.nome} está fazendo barulhos')

class Cachorro(Animal):
    def falar(self):
        print(f'O cachorro {self.nome} está latindo')

class Gato(Animal):
    def falar(self):
        print(f'O gato {self.nome} está miando')

teste = Animal("blayke")
print(teste.falar())

teste2 = Cachorro("Hazel")
print(teste2.falar())

teste3 = Gato("Naborá")
print(teste3.falar())