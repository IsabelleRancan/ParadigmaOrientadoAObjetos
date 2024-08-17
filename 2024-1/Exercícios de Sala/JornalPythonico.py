#

quantidade = int(input())

custos ={}

for i in range(quantidade):
        chv, vlr = input().split()
        vlr = int(vlr)
        custos [chv] = vlr

print (custos)

n_artigos = int(input())
artigos_caminho = []

for i in range(n_artigos): 
    artigos_caminho.append(input())
    i += 1

print (artigos_caminho)    


for i in range(n_artigos):
    valor_final = 0
    with open(artigos_caminho[i], 'r') as arquivo:
        conteudo = arquivo.read()
        for caractere in conteudo:
             if caractere in custos:
                  valor_final += custos[caractere]
    print(f'R${valor_final/100}')
