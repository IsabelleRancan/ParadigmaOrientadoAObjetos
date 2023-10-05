import abc
from datetime import datetime, timedelta
from enum import Enum

class Colaboradores(Enum):
    "criando a class colabroradores e adicionando valores dentro deles com o enum"
    AUTOR = "Autor"
    ATOR = "Ator"
    DIRETOR = "Diretor"
    EDITOR = "Editor"
    MUSICO = "Musico"

class Item (abc.ABC):
    "criando a classe principal e adicionando os principais atributos"
    def __init__(self, titulo, assunto, colaboradores):
        self.titulo = titulo 
        self.assunto = assunto 
        self.colaboradores = colaboradores 
        self.emprestado = None

    def Disponibilidade(self):
        """criando disponibilidade como o primeiro método depois do init porque ele vai 
        ser o meu método verificador
        
        Esse método retorna o valor de True quando o item NÃO ESTÁ EMPRESTADO e retorna 
        false quando o item ESTÁ EMPRESTADO"""
        # if self.emprestado == None:
        #     return True
        # else:
        #     return False
        return self.emprestado == None
    
    def Emprestar(self):
        """Verificando se um item está disponível ou não
        
        Se o método Disponibilidade() possui o valor TRUE, ou seja, a variável 
        estiver com o valor None, quer dizer que o livro pode ser emprestado, caso 
        contrário, ele não pode"""
        
        if self.Disponibilidade():
            self.emprestado == datetime.today()
            print ("Item emprestado com sucesso!")
        else:
            print ("O item não pôde ser emprestado!")

    def Devolver(self):
        if self.Disponibilidade() == False: #assim também funciona?
            self.emprestado == None
            print ("Item devolvido com sucesso!")
        else:
            print ("O item não pôde ser devolvido.")
         


