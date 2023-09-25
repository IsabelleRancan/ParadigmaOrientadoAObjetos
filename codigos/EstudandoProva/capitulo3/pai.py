class Pai:
    def __init__(self, nome):
        self.nome = nome
    
    def apresentar(self):
        print(f"Você é pai {self.nome}")

class Filho(Pai):
    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        print(f"Você é filho {self.nome}")

teste = Filho("João")
print(teste.apresentar())