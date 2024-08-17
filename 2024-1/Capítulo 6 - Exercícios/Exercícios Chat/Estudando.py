class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

# Dicionário com informações
informacoes_pessoa = {
    'nome': 'Carlos',
    'idade': 25,
    'endereco': ('Rua A', 123),
}

# Instanciando um objeto Pessoa
pessoa_instanciada = Pessoa(
    nome=informacoes_pessoa['nome'],
    idade=informacoes_pessoa['idade'],
    endereco=informacoes_pessoa['endereco']
)

# Acessando informações através do objeto
print(f"Nome: {pessoa_instanciada.nome}, Idade: {pessoa_instanciada.idade}")
print(f"Endereço: {pessoa_instanciada.endereco[0]}, Número: {pessoa_instanciada.endereco[1]}")

##Instanciando mais de um objeto:

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

# Dicionário com informações de pessoas
informacoes_pessoas = [
    {
        'nome': 'Carlos',
        'idade': 25,
        'endereco': ('Rua A', 123),
    },
    {
        'nome': 'Ana',
        'idade': 30,
        'endereco': ('Rua B', 456),
    },
    # Adicione mais informações de pessoas conforme necessário
]

# Lista para armazenar instâncias de Pessoa
pessoas_instanciadas = []

# Instanciando objetos Pessoa e adicionando à lista
for info in informacoes_pessoas:
    pessoa_instanciada = Pessoa(
        nome=info['nome'],
        idade=info['idade'],
        endereco=info['endereco']
    )
    pessoas_instanciadas.append(pessoa_instanciada)

# Acessando informações através da lista de objetos
for pessoa in pessoas_instanciadas:
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")
    print(f"Endereço: {pessoa.endereco[0]}, Número: {pessoa.endereco[1]}")
    print("---")
