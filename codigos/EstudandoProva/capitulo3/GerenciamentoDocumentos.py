import abc 

class Documentos(abc.ABC):
    "criando a classe abstrata Documentos"

    def __init__(self, autor, data, tamanho):
        "atributos que estarão presentes em todas as classes"
        self.autor = autor 
        self.data = data
        self.tamanho = tamanho

    @abc.abstractclassmethod
    def unidade_medida(self, medida):
        "método de medidas que estará presente em todas as classes, fazer mais tarde"
        pass

    def dimensoes(self, dimensoes):
        "método que retornará a quantidade de pixels se um documento tievr dimensões, fazer mais tarde"
        pass

class Pdf(Documentos):
    "nesse método não preciso mais pegar nenhum atributo novo"
    
    def __init__(self, autor, data, tamanho):
        super().__init__(autor,data, tamanho)

class DocsWord(Documentos):
    "nesse método não preciso mais pegar nenhum atributo novo"
    
    def __init__(self, autor, data, tamanho):
        super().__init__(autor,data, tamanho)

class Imagem(Documentos):
    "nesse método estou adicionando o parametro dimensoes"
    
    def __init__(self, autor, data, tamanho, dimensoes):
        self.dimensoes = dimensoes
        super().__init__(autor,data, tamanho)

class Video(Documentos):
    "nesse método estou adicionando dimencoes e a duração"
    
    def __init__(self, autor, data, tamanho, dimensoes, duracao):
        self.dimensoes = dimensoes
        self.duracao = duracao
        super().__init__(autor,data, tamanho)

