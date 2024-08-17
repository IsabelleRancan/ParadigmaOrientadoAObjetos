# 2 - Escreva uma função que receba uma lista de dicionários representando livros e retorne uma lista com os títulos dos livros 
#publicados após 2000

#dessa vez não criamos os parâmetros do dicionário por não ser necessário

def retorno_livros(lista_livros):
    #criando uma lista para adicionar apenas o título do livro 
    lista_apos2000 = []

    for livro in lista_livros:
        #no caso dos dicionarios, acessamos os parâmetros através dos colchetes 
        if livro["Ano"] > 2000:
            #acessando o nome do livro e adicionando na lista 
            lista_apos2000.append(livro["Nome"])

    print(f"Lista de livros publicados após o ano 2000", lista_apos2000)

#TESTANDO A API 
#criando o dicionário apenas na hora do teste e instanciando com as informações 
Livros = [
    {"Nome" : "Pássaro e Serpente", "Autor" : "Shelby Mahurin", "Ano" : 2016},
    {"Nome" : "Harry Potter", "Autor" : "J.K Roling ", "Ano" : 2000},
    {"Nome" : "Orgulho e Preconceito", "Autor" : "Jane Austen", "Ano" : 1779},
    {"Nome" : "Hipótese do Amor", "Autor" : "não lembro", "Ano" : 2020}
]       

resultado = retorno_livros(Livros)