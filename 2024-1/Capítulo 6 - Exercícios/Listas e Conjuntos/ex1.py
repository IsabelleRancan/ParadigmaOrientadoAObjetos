# Ler uma sequência de números, que se encerra com um número repetido. Escrever os números ordenadamente

def sequencia(): #criando uma função 
    numeros = set() #criando um conjunto vazio de set 

    while True:
        numero = int(input()) #recenedo numeros do usuário e convertendo para inteiro  
        if numero in numeros: #se o número já existir no set ele para
            break
        else:
            numeros.add(numero) #adicionando numero no conjunto 

    numeros_ordenados = sorted(numeros)
    print("Sequencia: ", numeros_ordenados)

#chamando a função
sequencia()