#Um anagrama é uma palavra ou frase formada reorganizando as letras de outra palavra ou frase, usando todas as letras originais 
#exatamente uma vez. Em outras palavras, as palavras ou frases são anagramas se tiverem as mesmas letras, mas em ordens diferentes. 
#Exemplos de anagramas: "amor" e "roma"; "listen" e "silent"; "ator" e "rota".
#Ler um número n seguido por n pares de palavras, e, para cada par, escrever "S" ou "N" caso sejam anagramas ou não.

def pares_palavras():
    n = int(input("Digite um número: "))

    for i in range(n):
        palavra1 = str(input("Digite a primeira palavra: ")).lower
        palavra2 = str(input("Digite a segunda palavra: ")).lower

        palavra_1 = set(palavra1.slpit())
        palavra_2 = set(palavra2.slpit())

        if 