import abc 

class Documentos(abc.ABC):
    "criando a classe abstrata Documentos"

    def __init__(self, autor, data, tamanho):
        "atributos que estarão presentes em todas as classes"
        self.autor = autor 
        self.data = data
        self.tamanho = tamanho

    #@abc.abstractclassmethod
    def unidade_medida(self, medida):
        "método de medidas que estará presente em todas as classes, fazer mais tarde"
        pass


class Pdf(Documentos):
    "nesse método não preciso mais pegar nenhum atributo novo"
    
    def __init__(self, autor, data, tamanho):
        super().__init__(autor,data, tamanho)
        print ("----------------------------------------------------")
        print (f"Especificações sobre o documento PDF:")
        print (f"Autor: {self.autor}.")
        print (f"Data: {self.data}.")
        print (f"Tamanho: {self.tamanho}.")

class DocsWord(Documentos):
    "nesse método não preciso mais pegar nenhum atributo novo"
    
    def __init__(self, autor, data, tamanho):
        super().__init__(autor,data, tamanho)
        print ("----------------------------------------------------")
        print (f"Especificações sobre o documento Word:")
        print (f"Autor: {self.autor}.")
        print (f"Data: {self.data}.")
        print (f"Tamanho: {self.tamanho}.")


class Imagem(Documentos):
    "nesse método estou adicionando o metodo dimensoes"
    
    def __init__(self, autor, data, tamanho, altura, largura):
        super().__init__(autor,data, tamanho)
        self.altura=altura
        self.largura=largura
        print ("----------------------------------------------------")
        print (f"Especificações sobre o documento: ")
        print (f"Autor: {self.autor}.")
        print (f"Data: {self.data}.")
        print (f"Tamanho: {self.tamanho}.")
        print (f"Pixels: {self.dimensoes()}.")


    def dimensoes(self):
        return self.altura * self.largura

class Video(Imagem):
    "essa classe herda imagem para podermos manipular os atributos no método dimensoes"
    
    def __init__(self, autor, data, tamanho, altura, largura, duracao):
        self.duracao = duracao
        super().__init__(autor, data, tamanho, altura, largura)
        print (f"Duração: {self.duracao}.")

    def dimensoes(self):
        return super().dimensoes()

teste = Pdf("ana", "06/05/2004", 5)
print()

teste2 = Imagem("isa", "06/05/2004", 5, 10, 5)
print()

teste3 = Video("maria", "20/05/1975", 2, 20, 10, 120)
print()