import time

class Pessoa:
    "Criando a classe pessoa"

    def __init__(self, nome: str, data_nascimento: str):
        self.nome = nome
        # Convertendo a string da data de nascimento para um objeto struct_time
        self.data_nascimento = time.strptime(data_nascimento, "%d-%m-%Y")

    @property
    def idade(self):
        # Obtendo a data atual
        data_atual = time.gmtime()

        # Calculando a diferença em anos entre a data atual e a data de nascimento
        idade = data_atual.tm_year - self.data_nascimento.tm_year

        # Verificando se o aniversário já ocorreu este ano
        if (data_atual.tm_mon, data_atual.tm_mday) < (self.data_nascimento.tm_mon, self.data_nascimento.tm_mday):
            idade -= 1

        return idade

    def __str__(self):
        return f"Nome: {self.nome}, Data de Nascimento: {time.strftime('%d-%m-%Y', self.data_nascimento)}, Idade: {self.idade}"

# Exemplo de uso
pessoa1 = Pessoa('Isabelle', '06-05-2004')
print(pessoa1)

pessoa2 = Pessoa('Ana', '01-01-2000')
print(pessoa2)