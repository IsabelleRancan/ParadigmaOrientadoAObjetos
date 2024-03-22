#Ler duas frases, uma em cada linha. Escrever em uma linha as palavras da primeira frase que não ocorrem na segunda frase. 
#Escrever em outra linha as palavras da primeira frase que ocorrem na segunda frase.

def frases():
    frase1 = str(input("Digite a frase 1: "))
    frase2 = str(input("Digite a frase 2: "))

    palavras1 = set(frase1.split()) #transformando a lista em set e dividindo a frase em palavras
    palavras2 = set(frase2.split())

    print("Palavras da primeira frase que não ocorrem na segunda frase: ", palavras1.difference(palavras2))
    print("Palavras da primeira frase que ocorrem na segunda frase: ", palavras1.intersection(palavras2))

frases()