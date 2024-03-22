# 1 - Crie um dicionário representando um livro com os campos titulo, autor e ano. Imprima as informações do livro

Livro = [
    {"Nome" : "Pássaro e Serpente", "Autor" : "Shelby Mahurin", "Ano" : 2016},
    {"Nome" : "Harry Potter", "Autor" : "J.K Roling ", "Ano" : 2000},
    {"Nome" : "Orgulho e Preconceito", "Autor" : "Jane Austen", "Ano" : 1779}
]

for livro in Livro:
    print (f"Livro: {livro['Nome']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}")