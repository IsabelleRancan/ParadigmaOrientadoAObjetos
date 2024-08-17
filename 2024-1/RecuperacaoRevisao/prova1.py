#tentando refazer a prova um

biblioteca = [
("Python for Beginners", "John Smith", 2020, 300),
("Data Science Essentials", "Jane Doe", 2019, 450),
("History of Science", "Robert Johnson", 2018, 250),
("Artificial Intelligence in Practice", "Alice Williams", 2021, 380),
("Literary Classics", "David Brown", 2017, 500)
]

#recebe uma tupla com os dados do livro como argumento e o insere na lista.
def adicionar_livro(biblioteca, livro):
    biblioteca.append(livro)


# recebe o título e o nome do autor como argumentos e exclui da lista o livro correspondente.
def excluir_livro(bibioteca, titulo, autor):
    for livro in biblioteca:
        if livro[0] == titulo and livro[1] == autor:
            bibioteca.remove(livro)
            break

#recebe o nome de um autor como argumento e retorna uma lista contendo os títulos dos livros desse autor. Se o autor não tiver nenhum 
# livro na biblioteca, a função deve retornar uma lista vazia.
def consultar_livros_por_autor(biblioteca, autor):
    livros_autor = []
    for livro in biblioteca:
        if livro[1] == autor: 
            livros_autor.append(livro[0])
    return livros_autor

#recebe um ano como argumento e retorna uma lista contendo os títulos dos livros publicados nesse ano.
def livros_publicados_no_ano(biblioteca, ano):
    livros_ano = []
    for livro in biblioteca:
        if livro[2] == ano: 
            livros_ano.append(livro[0])
    return livros_ano 

#calcula e retorna a média do número de páginas de todos os livros na biblioteca.
def calcular_media_paginas(biblioteca):
    total_paginas = 0
    for livro in biblioteca:
        total_paginas += livro[3];
    return total_paginas / len(biblioteca)

#recebe um número de páginas como argumento e retorna uma lista de tuplas composta pelo título e o número de páginas dos livros que têm 
# mais páginas que o argumento.
def livros_maiores_que(biblioteca, pagina): 
    livros_maiores = []
    for livro in biblioteca:
        if livro[3] > pagina: 
            livros_maiores.append((livro[0], livro[3]))
    return livros_maiores

novo_livro = ("Alice no País das Maravilhas", "John Carol", 1980, 75)
adicionar_livro(biblioteca, novo_livro)
print(f"Nova lista: ", biblioteca)

excluir_livro(biblioteca, "History of Science", "Robert Johnson")
print(f"Lista com livro excluido: ", biblioteca)

pesquisa_autor = "Jane Doe"
resultado = consultar_livros_por_autor(biblioteca, pesquisa_autor)
print(f"Pesquisa Autor: ", resultado)

pesquisa_ano = 2020
resultado_ano = livros_publicados_no_ano(biblioteca, pesquisa_ano)
print(f"Livros do ano pesquisado: ", resultado_ano)

media = calcular_media_paginas(biblioteca)
print(f"A média de páginas da biblioteca é: ", media)

maiores = livros_maiores_que(biblioteca, 300)
print(f"Lista de livros maiores que o numero de paginas solicitado: ", maiores)