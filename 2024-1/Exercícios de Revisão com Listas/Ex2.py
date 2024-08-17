#Crie uma função que recebe uma lista de palavras e retorna a quantidade de palavras que começam com uma letra específica.

def palavras_especiais(lista, letra):
    letra = letra.lower()
    c = 0
    for palavra in lista:
        palavra = palavra.lower()
        if palavra.startswith(letra):
            c += 1
    return(f"A quantidade de palavras que começam com a letra '{letra}' é igual a: ", c)

#Testando a api 

teste = ["testando", "Tem", "prova", "hoje"]
letrinha = "t"
codigo = palavras_especiais(teste, letrinha)
print(codigo)