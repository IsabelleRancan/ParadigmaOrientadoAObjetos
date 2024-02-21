import abc 
from enum import Enum 

class Telefone_tipo(Enum):
    CASA = "Casa"
    TRABALHO = "Trabalho"
    CELULAR = "Celular"
    
class Email_tipo(Enum):
    PESSOAL = "Pessoal"
    TRABALHO = "Trabalho"
    
class Endereco:
    def __init__(self, rua, numero, complemento, cidade, cep):
        self.rua = rua 
        self.numero = numero 
        self.complemento = complemento
        self.cidade = cidade
        self.cep = cep
        print(f"{self.rua}, {self.numero}, {self.complemento} {self.cidade} {self.cep}")

class Contato(abc.ABC):
    def __init__(self, nome, telefone, email, rua, numero, complemento, cidade, cep):
        self.nome = nome
        self. telefone = telefone 
        self.email = email
        self.endereco = Endereco(rua, numero, complemento, cidade, cep)
        print(f"{self.nome}, {self.telefone}, {self.email}, {self.endereco}")
    
    def adicionar():
        pass
    
    def excluir():
        pass
    
    def editar():
        pass 
    
    def buscar():
        pass

endereco1 = Endereco("rua da alegria", 200, "portão", "Três Lagoas", 70000)
testeendereco = endereco1
print(endereco1)

print(Contato("Isa", 1111, "isa@", "rua da alegria", 100, "sla", "sla", 9999999))

