#implementando as informações

biblioteca = [
 ("Python for Beginners", "John Smith", 2020, 300),
 ("Data Science Essentials", "Jane Doe", 2019, 450),
 ("History of Science", "Robert Johnson", 2018, 250),
 ("Artificial Intelligence in Practice", "Alice Williams", 2021, 380),
 ("Literary Classics", "David Brown", 2017, 500)
]

#adicionar_livro: recebe uma tupla com os dados do livro como argumento e o insere na lista.
def adicionar_livro(novo_livro): #elemento  que vai ser adicionado, precisa ser uma tupla já
    biblioteca.append(novo_livro)
    return novo_livro #pra ele retornar o livro adicionado

#excluir_livro: recebe o título e o nome do autor como argumentos e exclui da lista o livro 
def excluir_livro(titulo, autor): #recebe os argumentos titulo e autor
    for item in biblioteca: #loop para iterar sobre a biblioteca
        if item[0] == titulo and item[1] == autor: #se item possuir titulo igual ao titulo informmado e autor 
            biblioteca.remove(item) #acessando a lista, e removendo o item encontrado
            return ("Nova lista atualizada", biblioteca) #retornando a lista atualizada 
    return ("Livro não encontrado") #se não encontrar ele retorna essa mensagem de erro 

#consultar_livros_por_autor: recebe o nome de um autor como argumento e retorna uma lista
#contendo os títulos dos livros desse autor. Se o autor não tiver nenhum livro na biblioteca, a função deve
#retornar uma lista vazia.
def livros_por_autor(autor):
    lista_livros = []

    for item in biblioteca:
        if item[1] == autor: 
            lista_livros.append(item[0])
            return("Livros do autor: ", lista_livros)
    return (lista_livros)

#livros_publicados_no_ano: recebe um ano como argumento e retorna uma lista contendo os títulos dos livros publicados nesse ano
def livros_publicados_no_ano(ano):
    lista_livros = []

    for item in biblioteca:
        if item[2] == ano:
            lista_livros.append(item[0])
            return(f"Livros publicados no ano: ", lista_livros)
    return(lista_livros)

#calcular_media_paginas: calcula e retorna a média do número de páginas de todos os livros na biblioteca
def calcular_media_paginas():
    numero_paginas = 0

    for item in biblioteca:
        numero_paginas += item[3]

    media = numero_paginas / (len (biblioteca))
    return media

#livros_maiores_que: recebe um número de páginas como argumento e retorna uma lista de tuplas 
#composta pelo título e o número de páginas dos livros que têm mais páginas que o argumento.
def livros_maiores_que(paginas):
    lista_livros = []

    for item in biblioteca:
        if item[3] > paginas:
            lista_livros.append((item[0], item[3]))
    return("Livros com número de páginas maior do que o informado: ", lista_livros)
    return("Nenhum livro encontrado")


            

#TESTANDO API 
livro1 = ("Titulo", "ana", 2002, 250) #tranformando os dados do livro em uma tupla
adicionar_livro(livro1) #adicionando a tupla na nossa lista
print(biblioteca)

teste = excluir_livro("Titulo", "ana")
print(teste)

teste_autor_certo = livros_por_autor("Jane Doe")
print(teste_autor_certo)
teste_autor = livros_por_autor("Jan Doe")
print(teste_autor)

teste_ano = livros_publicados_no_ano(2020)
print(teste_ano)

print("A média do numero de páginas da biblioteca é de: ", calcular_media_paginas()) #já que eu não pessei nenhum valor, eu posso chamar a função diretamente

npaginas = livros_maiores_que(300)
print(npaginas)