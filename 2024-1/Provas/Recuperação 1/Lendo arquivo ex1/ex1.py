#vai receber dois arquivos de texto e verificar qual deles possuí o maior número de palavras

with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    arquivo_1 = list(conteudo.split())

with open('texto2.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    arquivo_2 = list(conteudo.split())
    
    if len(arquivo_1) > len(arquivo_2):
        print(f"O primeiro arquivo de texto tem mais palavras que o segundo! Com {len(arquivo_1)} palavras!")
    elif len(arquivo_1) < len(arquivo_2):
        print(f"O segundo arquivo de texto tem mais palavras que o primeiro! Com {len(arquivo_2)} palavras!")
    else: print("Os dois documentos de texto possuem o mesmo número de palavras!")
