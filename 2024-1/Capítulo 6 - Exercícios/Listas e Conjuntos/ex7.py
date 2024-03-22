#Um heterograma é uma palavra ou frase em que nenhuma letra do alfabeto ocorre mais de uma vez.
#Ler um número n, seguido por n frases, uma em cada linha. Para cada frase, escrever "S" ou "N" caso seja heterograma ou não

def heterograma():
    n = int(input("Digite um número: "))

    for i in range(n):
        frase = str(input(f"Digite a frase {i+1}: "))
        frase = frase.replace(" ", "").lower() #removendo os espaços e tranformando tudo para minusculas 
        letras_na_frase = set(frase) #nesse caso eu n preciso usar o list 

        if len(letras_na_frase) == len (frase):
            print("S")
        else:
            print("N")
        
heterograma()