#Ler um caminho para um novo arquivo de texto e o conteúdo a ser salvo neste arquivo de texto, até encontrar um EOF. 
#Caso o usuário informe um caminho para um arquivo existente, avisá-lo, e encerrar o programa.
import os #importando o módulo 'os' que interage com o sistema operacional

titulo = str(input("Digite o título do arquivo a ser criado:  "))
if os.path.exists(titulo): #essa linha verifica se o arquivo já existe dentro da pasta ou não x
    print(f'Já existe um arquivo com o nome {titulo}')
else: 
    with open(titulo, 'w') as arquivo: 
        print("Digite o conteúdo a ser salvo: ")

        while True: 
            texto = str(input())
            if texto == "":
                break;
        
            conteudo = arquivo.write(texto + '\n')

    #lendo o arquivo
    with open(titulo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(f"\n\nO arquivo {titulo} possuí o seguinte texto: \n{conteudo}")