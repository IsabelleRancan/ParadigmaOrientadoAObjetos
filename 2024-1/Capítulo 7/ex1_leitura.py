#Ler um caminho para um arquivo de texto e escrever o conteúdo do arquivo.

with open ('texto.txt', 'r') as arquivo: 
    conteudo = arquivo.read()
    print(conteudo)