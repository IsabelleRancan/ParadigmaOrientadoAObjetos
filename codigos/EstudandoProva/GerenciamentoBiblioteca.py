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

    @abc.abstractmethod 
    def Prazo(self):
        pass

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
        if self.Disponibilidade():
            print ("O item não pôde ser devolvido.")        
        else:
            self.emprestado == None
            print ("Item devolvido com sucesso!")

    def PrazoDevolucao(self):
        if self.Disponibilidade():
            print ("O item não possui um prazo de devolução ativo")        
        else:
            data_devolucao = self.emprestado + timedelta(days=self.prazo)
            hoje = datetime.today()
            dias = (data_devolucao - hoje).days
            return dias

    def informacoes(self):
        print ("----------------------------------------------------")
        print (f" Título: {self.titulo}")
        print (f" Assunto: {self.assunto}")
        print (f" Colaboradores: {self.colaboradores}") #testar se esse trem de colaboradores funciona assim ou se eu tenho que colocar a função 
        print (f" Devolução: {self.PrazoDevolucao()}")

class Livro (Item):
    "criando a subclasse Livro e atribuindo o valor de prazo pra ela"

    prazo = 21 #isso tá certo ou eu preciso sobrescrever o método todo para poder atribuir o valor 

    def __init__(self, titulo, assunto, colaboradores, isbn):
        "chamando o método init da classe pai e adicionando valor ao parametro novo"
        self.isbn = isbn
        super().__init__(titulo, assunto, colaboradores)

    def informacoes(self):
        "chamando o método da classe principal e adicionando o parametro que estava faltando - POLIMORFISMO"
        super().informacoes()

        print(f"ISBN: {self.isbn}")

class Dvd (Item):

    prazo = 7

    def __init__(self, titulo, assunto, colaboradores, generos):
        "chamando o método init da classe pai e adicionando valor ao parametro novo"
        self.generos = generos
        super().__init__(titulo, assunto, colaboradores)

    def informacoes(self):
        "chamando o método da classe principal e adicionando o parametro que estava faltando - POLIMORFISMO"
        super().informacoes()

        print(f"Gêneros: {self.generos}")

class Revista (Item):

    prazo = 14

    def __init__(self, titulo, assunto, colaboradores, volume, edicao):
        "chamando o método init da classe pai e adicionando valor ao parametro novo"
        self.volume = volume
        self.edicao = edicao
        super().__init__(titulo, assunto, colaboradores)

    def informacoes(self):
        "chamando o método da classe principal e adicionando o parametro que estava faltando - POLIMORFISMO"
        super().informacoes()

        print(f"Volume: {self.volume}")
        print(f"Edição: {self.edicao}")

#teste_colaborador = ("Ana", Colaboradores.AUTOR)
#teste_colaborador2 = ("Maria", Colaboradores.EDITOR)

#colab = (teste_colaborador, teste_colaborador2)
#livro1 = Livro("Harry Potter", "Fantasia", "teste", 12345)