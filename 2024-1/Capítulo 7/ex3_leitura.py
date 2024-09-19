#Ler um caminho para um arquivo de texto e escrever quantas palavras ele possui.

nome_arquivo = str(input('Digite o nome do arquivo: '))

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    print(len(palavras)
)