#Implemente uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números pares

n_pares = []
def numeros_pares(numeros):
    for i in numeros:
        if i % 2 == 0:
            n_pares.append(i)
    return n_pares 

#testando api 

n = [1,2,3,4,5,6,7,8,9]
teste = numeros_pares(n)
print(teste)