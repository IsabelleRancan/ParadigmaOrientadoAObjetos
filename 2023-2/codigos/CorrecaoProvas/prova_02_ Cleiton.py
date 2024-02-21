#    __________            ______________               _______________________           _________________                                                                                                                                                                  
#   | <<Enum>> |          |              |             |    <<abstract>>       |         |     Livros      |                                                                                                                                    
#   |  Papel   |          |  Colaborador |             |________Item___________|         |_________________|                                                                                                                                                 
#   |__________|          |______________|             | +titulo : str         |<--------| +ISSN: str      |                                                                                                                                                          
#   | Ator     |          | +nome : str  |             | +assunto : int        |         |_________________|                                                                                                                                                       
#   | Autor    |1________1| +papel:str   |N___________1| +prazo : int          |         |_________________|                                                                                                                                                                           
#   | Diretor  |          |______________|             | +colaboradores : list |          _________________                ________________                                                                                                                                              
#   | Editor   |          |______________|             |_______________________|         |       DVD       |              |   <<Enum>>     |                                                                                                                    
#   | Musico   |                                       | +emprestar()          |<--------|_________________|              |    Genero      |                                                                                                      
#   |__________|                                       | +devolver()           |         | +generos : list |1____________1|________________|                                                                                                                               
#                                                      | +disponivel()         |         |_________________|              | Drama          |                                                                                                            
#                                                      | +verificar_devolucao()|          _________________               | Comedia        |                                                                                                                
#                                                      | +obter_info()         |         |     Revista     |              | Terror         |                                                                                          
#                                                      |_______________________|<--------|_________________|              | Musical        |                                                                                                                   
#                                                                                        | +volume : int   |              |________________|                                                                                                
#                                                                                        | +edicao : int   |                                                                                                              
#                                                                                        |_________________|

import abc
from datetime import datetime, timedelta
from enum import Enum

#Classe papel herda de Enum, clase do Python que atribui uma lista de valores definidos
class Papel(Enum):
    #informa valores pré-fixados no formato "name = value"
    AUTOR = "autor"
    ATOR = "ator"
    DIRETOR = "diretor"
    EDITOR = "editor"
    MUSICO = "musico"

#Classe Colaborador define um objeto colaborador contendo atributos nome e papel, onde papel recebe um objeto Papel(Enum)
class Colaborador:
    def __init__(self, nome, papel):
        self.nome = nome
        self.papel = papel

#Classe Genero herda de Enum, instanciando uma lista de valores definidos
class Genero(Enum):
    DRAMA = "Drama"
    COMEDIA = "Comedia"
    TERROR = "Terror"
    MUSICAL = "Musical"

#Classe Item é uma classse abstrata, que por padrão não deve instanciar objetos, apenas ser herdada pelos sua classes filhas
#com intuito de possibilitar reaprovitamento de codigo, ja que tudo que consta nela será usado em cada classe filha.
class Item(abc.ABC):
    def __init__(self, titulo, assunto, colaboradores):
        self.titulo = titulo
        self.assunto = assunto
        self.colaboradores = colaboradores
        self.data_emprestimo = None

    #Informa que esse método terá comportamento de um atributo
    @property
    #Força a classe filha a instanciar esse metodo
    @abc.abstractmethod
    def prazo(self):
        #não implementa nada, passando a responsabilidade a classe filha pra resolver esse BO
        pass
    #Verifica a disponibilidade do item
    def disponivel(self):
        #verifica se o atributo "data_emprestimo" é igual a "None" e devolve True ou False dependendo do que encontrar
        return self.data_emprestimo == None
    
    #seta o emprestimo do item
    def emprestar(self):
        #solicita a resposta do metodo "disponivel()" esperando receber TRue ou False
        if self.disponivel():
            #se True 
            #aplica a data atual ao atributo data_emprestimo 
            self.data_emprestimo = datetime.today()
            #printa o atributo titulo do obj, adicionando "emprestado"
            print(self.titulo, "emprestado!")
        else:
            #se False
            #printa "não é possível emprestar" + o atributo titulo do obj
            print("não é possível emprestar", self.titulo)

    #seta a devolução do Item
    def devolver(self):
        #solicita a resposta do metodo "disponivel()" esperando receber TRue ou False
        if self.disponivel():
            #se True
            #printa o atributo titulo do obj, adicionando "não está emprestado para ser devolvido"
            print(self.titulo, "não está emprestado para ser devolvido")
        else:
            #se False
            #seta data_emprestimo que continha a data do emprestimo anterior pra None
            self.data_emprestimo = None
            #printa o atributo titulo do obj, adicionando "devolvido!" 
            print(self.titulo, "devolvido!")

    
    
    def verificar_devolucao(self):
        #invoca o metodo "disponivel()" e se receber True, ja retorna "None"
        if self.disponivel():
            return None
        #se não retornou, segue o codigo, calculando a data da devolução (data_emprestimo + prazo)
        prazo_maximo = self.data_emprestimo + timedelta(days=self.prazo)
        #pega a data de hoje
        hoje = datetime.today()
        #retorna a diferenca entre a data de emprestimo e a data de hoje
        #a função ja retornará negativo automaticamente se a data de devolução for menor que a data de hoje
        return (prazo_maximo - hoje).days

    
    def obter_info(self):
        #Printa todos atributos do objeto item
        print("Título:", self.titulo)
        print("Assunto:", self.assunto)

        #obtem o atrifuto prazo pelo metodo "verificar_devolucao()" ja que esse atributo foi passado as classe filhas
        #a responsabilidade de atribui-lo de maneira diverente para cada uma
        print("Prazo:", self.verificar_devolucao())

        #itera por colaboradores...
        print("Colaboradores:")
        for colaborador in self.colaboradores:
            "como funciona isso e  que tem a ver a class enum lá em cima?"
            #...printando seu atributo nome
            print("    ", colaborador.nome)


#HERANÇA
#classe filha DVD herda de Item
class DVD(Item):
    "ele não precisa colocar o método prazo e colocar o prazo dentro dele?"
    #define o atributo "prazo", no qual a superclasse delegou a responsabilidade para as filhas
    prazo = 7
    #solicita os valores dos atributos por parametro, onde requer todos os atributos da classe herdada ( titulo, assunto,colaboradores)
    #  + os atributos particulares desta classe  (genero)
    def __init__(self, titulo, assunto, genero, colaboradores):
        #acrescenta o atributo genero ao objeto instanciado
        self.genero = genero
        #passa os demais atributos para o meto init da classe herdada fazere sua parte
        super().__init__(titulo, assunto, colaboradores)

    def obter_info(self):
        #POLIMORFISMO
        #chama o metodo "obter_info()" da superclasse, e o modifica acrescentando...
        super().obter_info()
        #... esta opção para printar o atributo particular da classe filha "genero"
        print("Generos:")
        for genero in self.genero:
            "como ele vai saber que genero é uma list? e como o usuário vai poder declarar mais que um?"
            print("    ", genero.value)

#as demais classe seguem o exato raciocinio da classe DVD...
class Livro(Item):
    prazo = 21

    def __init__(self, titulo, assunto, isbn, colaboradores):
        self.isbn = isbn
        super().__init__(titulo, assunto, colaboradores)

    def obter_info(self):
        super().obter_info()
        print("ISBN:", self.isbn)


class Revista(Item):
    prazo = 14

    def __init__(self, titulo, assunto, volume, edicao, colaboradores):
        self.volume = volume
        self.edicao = edicao
        super().__init__(titulo, assunto, colaboradores)

    def obter_info(self):
        super().obter_info()
        print("Volume:", self.volume)
        print("Edição:", self.edicao)



#instanciação de objetos para teste.
#(ver no terminal)
print('======================================================================')
"entender essa instância aqui*"
colab_pedro = Colaborador("Pedro", Papel.ATOR)
colab_henrique = Colaborador("Henrique", Papel.AUTOR)
colaboradores = [colab_pedro, colab_henrique]

L1 = Livro("A pedra do pedro", "ficção", "12382388238", colaboradores)

L1.emprestar()

L1.obter_info()


if L1.disponivel():
    print('Situação: Disponivel')
else:
    print('Situação: Emprestado')

    if (L1.verificar_devolucao() > 0):
        print("Ele será entregue em ", L1.verificar_devolucao(), "dias")
    else:
        print("Ele já deveria ter sido entregue!")

print('======================================================================')


print('\n======================================================================')

gen_comedia = Genero.COMEDIA
gen_dramama = Genero.DRAMA
generos_D1 = [gen_comedia, gen_dramama]

colab_amilton = Colaborador('Amiltom', Papel.DIRETOR)
colaboradores_D1 = [colab_amilton]

D1 = DVD("A volta dos que não foram", "Longa metragem", generos_D1, colaboradores_D1)

D1.emprestar()

D1.obter_info()

D1.devolver()


if D1.disponivel():
    print('Situação: Disponível')
else:
    print('Situação: Emprestado')

    if (D1.verificar_devolucao() > 0):
        print("Ele será entregue em ", D1.verificar_devolucao(), "dias")
    else:
        print("Ele já deveria ter sido entregue!")

print('======================================================================')


print('\n======================================================================')

colab_maria = Colaborador('Maria', Papel.EDITOR)
colaboradores_R1 = [colab_maria]

R1 = Revista("Caras de Paus", "Papel inútil", 5, 3, colaboradores_R1)

R1.emprestar()

R1.obter_info()


if R1.disponivel():
    print('Situação: Disponível')
else:
    print('Situação: Emprestado')

    if (R1.verificar_devolucao() > 0):
        print("Ele será entregue em ", R1.verificar_devolucao(), "dias")
    else:
        print("Ele já deveria ter sido entregue!")

print('======================================================================')
