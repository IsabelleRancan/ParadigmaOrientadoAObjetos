from dataclasses import dataclass

#2 - Escreva uma função que receba uma lista de produtos e retorne o preço total de todos os produtos.

#criando a dataclass com os campos de Produto
@dataclass
class Produto:
    nome: str 
    preco: float 
    quantidade: int 

def soma_produtos(lista_produtos):
    preco_total = 0

    for product in lista_produtos:
        preco_total += product.preco * product.quantidade
        
    return preco_total
    
#TESTANDO A API 
meus_produtos = [
    Produto("Shampoo", 11.50, 1),
    Produto("Condicionador", 12.00, 2), 
    Produto("Sabonete", 2.50, 5)
]

resultado = soma_produtos(meus_produtos)
print(f"O preço total dos produtos é de: ", resultado)


