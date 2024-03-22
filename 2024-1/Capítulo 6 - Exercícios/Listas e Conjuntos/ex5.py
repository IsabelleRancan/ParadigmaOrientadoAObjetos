#Ler dois arquivos de texto diferentes. Escrever as palavras presentes em pelo menos um dos arquivos, sem duplicatas.

def frases():
    frase1 = str(input("Digite a primeira frase: "))
    frase2 = str(input("Digite a segunda frase: "))

    palavras1 = set(frase1.split())
    palavras2 = set(frase2.split())

    print("Plavras presentes em pelo menos uma frase: ", palavras1.union(palavras2))

frases()