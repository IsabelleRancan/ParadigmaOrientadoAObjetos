#Ler um caminho para um arquivo de texto e uma palavra-chave. 
#Escrever quantas vezes a palavra-chave ocorre.

nome_arquivo = str(input('Digite o nome do arquivo: '))
palavrachave = str(input('Digite a palavra-chave: '))
total = 0

with open (nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()

    for palavra in palavras: 
        if palavra == palavrachave:
            total += 1 
    print(f"\n Foram encontradas {total} palavras-chave no texto.")
    print(palavras)