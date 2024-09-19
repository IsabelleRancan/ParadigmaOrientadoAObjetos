#concatena_strings: recebe uma string inicial e uma quantidade arbitrária de outras strings como argumentos posicionais. 
# Retorna a concatenação de todas as strings recebidas.

def concat(*args):
    c = ",".join(args) #unando , como critério de junção
    return c

print(concat('a','b','c','d'))