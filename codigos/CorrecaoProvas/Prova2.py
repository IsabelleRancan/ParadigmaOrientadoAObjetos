import abc
from datetime import datetime, timedelta
from enum import Enum


class Papel(Enum):
    AUTOR = "autor"
    ATOR = "ator"
    DIRETOR = "diretor"
    EDITOR = "editor"
    MUSICO = "musico"


class Colaborador:
    def __init__(self, nome, papel):
        self.nome = nome
        self.papel = papel


class Item(abc.ABC):
    def __init__(self, titulo, assunto, colaboradores):
        self.titulo = titulo
        self.assunto = assunto
        self.colaboradores = colaboradores
        self.data_emprestimo = None

    @property
    @abc.abstractmethod
    def prazo(self):
        pass

    def emprestar(self):
        self.data_emprestimo = datetime.today()

    def devolver(self):
        self.data_emprestimo = None

    def disponivel(self):
        return self.data_emprestimo == None

    def verificar_devolucao(self):
        if self.disponivel():
            return None
        prazo_maximo = self.data_emprestimo + timedelta(days=self.prazo)
        hoje = datetime.today()
        return (prazo_maximo - hoje).days

    def obter_info(self):
        print("Título:", self.titulo)
        print("Assunto:", self.assunto)
        print("Prazo:", self.verificar_devolucao())
        print("Colaboradores:")
        for colaborador in self.colaboradores:
            print("    ", colaborador.nome)


class Livro(Item):
    prazo = 21

    def __init__(self, titulo, assunto, isbn, colaboradores):
        self.isbn = isbn
        super().__init__(titulo, assunto, colaboradores)

    def obter_info(self):
        super().obter_info()
        print("ISBN:", self.isbn)


colab1 = Colaborador("Pedro", Papel.ATOR)
colab2 = Colaborador("Henrique", Papel.AUTOR)
colaboradores = [colab1, colab2]
item = Item("um titulo", "um assunto", colaboradores)

item.obter_info()