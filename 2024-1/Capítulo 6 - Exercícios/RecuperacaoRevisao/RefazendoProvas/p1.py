biblioteca = [
    ("Python for Beginners", "John Smith", 2020, 300),
    ("Data Science Essentials", "Jane Doe", 2019, 450),
    ("History of Science", "Robert Johnson", 2018, 250),
    ("Artificial Intelligence in Practice", "Alice Williams", 2021, 380),
    ("Literary Classics", "David Brown", 2017, 500)
]

def adicionar_livro(biblioteca, novo_livro):
    biblioteca.append(novo_livro)

def excluir_livro(biblioteca, titulo, autor):
    for livro in biblioteca:
        if livro[0] == titulo and livro[1] == autor:
            biblioteca.remove(livro)
            break 

def consultar_livros_por_autor(biblioteca, autor):
    livros_autor = []
    for livro in biblioteca:
        if livro[1] == autor: 
            livros_autor.append(livro[0])
        return livros_autor



livro1 = ("Narnia", "C.S. Lewis", 1890, 700)
adicionando_livro = adicionar_livro(biblioteca, livro1)
print(biblioteca)

excluir = excluir_livro(biblioteca, 'History of Science', 'Robert Johnson')
print(f"Lista com livro excluido: ", biblioteca)

consultar = consultar_livros_por_autor(biblioteca, 'John Smith')
print(consultar)