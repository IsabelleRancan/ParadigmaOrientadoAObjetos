class Veiculo:
    def __init__(self, marca, ano):
        self. marca  = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, ano, modelo):
        super().__init__(marca, ano)
        self. modelo = modelo

    def detalhes(self):
        print(f"{self.marca}, {self.ano} , {self.modelo}")

teste = Carro("McLaren" , 2015, "Sport")
print(teste.detalhes())
