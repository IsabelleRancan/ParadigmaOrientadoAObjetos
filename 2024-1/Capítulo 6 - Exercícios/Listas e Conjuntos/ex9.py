#Lista proibida. Ler um número n, seguido por n palavras "proibidas". Depois, ler um número m, 
#seguido por m frases, uma em cada linha. Para cada frase, escrever "PERMITIDO" ou "CENSURADO" 
#caso haja palavras proibidas ou não.

def lista_proibida():
    n = int(input("Digite um número: "))

    palavras = []

    for i in range(n):
        p = str(input(f"Digite a {i+1}ª palavra proibida: ")).lower()
        palavras.append(p) 

    p_proibidas = set(palavras)

    m = int(input("Digite um número: "))
    frases_list = []

    for i in range(m):
        f = str(input(f"Digite a {i+1}ª frase: ")).lower()
        
        frases_list.append(f)

    for frase in frases_list:
        contem = 0
        for p in p_proibidas:
            if p in frase:
                contem += 1
        if contem > 0:
            print('CENSURADO')
        else:
            print('PERMITIDO')
        
                

lista_proibida()        