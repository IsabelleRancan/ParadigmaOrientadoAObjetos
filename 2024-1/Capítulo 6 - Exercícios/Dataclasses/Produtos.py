from dataclasses import dataclass

# 1 - Crie uma dataclass chamada Produto com os campos nome, preco e quantidade. Crie alguns produtos e imprima suas informações.

@dataclass
class Produto: 
    nome: str
    preco: float
    quantidade: int 

produtos = [
    Produto("Shampoo", 11.50, 1),
    Produto("Condicionador", 12.00, 2), 
    Produto("Sabonete", 2.50, 5)
]

for produto in produtos: 
    print(f"Produto: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")