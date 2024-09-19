# soma_numeros: Recebe uma quantidade arbitrária de números como argumentos posicionais. 
# Retorna a soma de todos os números passados como argumentos.

def soma(*args):
    return sum(args)

print(soma(1,2,3,5))
print(soma(2,4,6,8,10))