#Ler dois arquivos de texto diferentes. Escrever as palavras presentes em ambos os arquivos, sem duplicatas.

def frases():
    frase1 = str(input("Digite a primera frase: "))
    frase2 = str(input("Digite a segunda frase: "))

    palavras1 = set(frase1.split())
    palavras2 = set(frase2.split())

    print("Palavras nos textos: ", palavras1.intersection(palavras2))

frases()