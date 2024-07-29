#vai receber arquivos de texto e verificar o conteúdo de cada um e comparar qual possuí mais caracteres

where open('texto1.txt', 'r') as arquivo:
    conteudo = arquivo
    
    
    #if len(palavras_t1) > len(palavras_t2):
        #print("O primeiro arquivo de texto tem mais palavras que o segundo!")
    #else if len(palavras_t1) < len(palavras_t2):
        #print("O primeiro arquivo de texto tem menos palavras que o segundo!")
    #else print("Os dois documentos de texto possuem o mesmo número de palavras!")
