#Criando um catálogo de diferentes formas 
# -> IMPORTAÇÕES: 
#Tuplas nomeadas: from collections import namedtuple
 

#Tuplas 

Produtos = [("Reparador de Pontas", "cabelo", 13.00),
            ("Hidratante", "corpo", 35.50), 
            ("Esmalte", "unhas", 2.50)]


print(f"Catálogo")
#criando um for pra exibir todo o catálogo
for produto in Produtos:
    #criando variáveis para acessar cada informação separadamente 
    nome_produto, area_produto, preco_produto = produto 
    print(f"Produto: {nome_produto}, Area de uso: {area_produto}, Preço: {preco_produto}")

#Tupla nomeada 
    
from collections import namedtuple

Produto = namedtuple("Produto", ["Item", "area_uso", "preco"])
Produtos = [Produto("Reparador de pontas", "cabelo", 35.50),
            Produto("Hidratante", "corpo", 35.50),
            Produto("Esmalte", "unhas", 2.50)]

#criando um for pra exibir todo o catálogo
print("Catálogo usando tupla nomeada:")
for Produto in Produtos:
    print(f"Produto: {Produto.Item}, Area de uso: {Produto.area_uso}, Preço: {Produto.preco}") 

#Dicionários 
    
Produtos = [
    {"Nome_Produto" : "Reparador de Pontas", "Area_Uso": "Cabelo", "Preco" : 35.50},
    {"Nome_Produto" : "Hidratante", "Area_Uso": "corpo", "Preco" : 35.50},
    {"Nome_Produto" : "Esmalte", "Area_Uso": "Unhas", "Preco" : 2.50}
]

#criando um for pra exibir todo o catálogo
print("Catálogo usando dicionário:")
for Produto in Produtos:
    print(f"Produto: {Produto['Nome_Produto']}, Area de uso: {Produto['Area_Uso']}, Preço: {Produto['Preco']}")

#@dataclass 
    
from dataclasses import dataclass

@dataclass
class Produto:
    nome_produto: str
    area_uso: str 
    preco: float

produtos = [
    Produto("Reparador de Pontas", "cabelo", 13.00),
    Produto("Hidratante", "corpo", 35.50), 
    Produto("Esmalte", "unhas", 2.50)
]

#criando o for 
print("Catálogo com @dataclass:")
for produto in produtos:
    print(f"Produto: {produto.nome_produto}, Area de Uso: {produto.area_uso}, Preço: {produto.preco}")

#com make_dataclass
from dataclasses import make_dataclass

Produto = make_dataclass("Produto", ["nome_produto", "area_uso", "preco"])
produtos = [
    Produto("Reparador de Pontas", "cabelo", 13.00),
    Produto("Hidratante", "corpo", 35.50), 
    Produto("Esmalte", "unhas", 2.50)
]

print("Catálogo com make_dataclass")

#criando o for 
for produto in produtos:
    print(f"Produto: {produto.nome_produto}, Area de Uso: {produto.area_uso}, Preço: {produto.preco}")
