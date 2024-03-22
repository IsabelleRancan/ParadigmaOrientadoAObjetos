#Um pangrama é uma frase em que são usadas todas as letras do alfabeto de determinada língua. Exemplo de pangrama em inglês: 
#The quick brown fox jumps over the lazy dog. Exemplo de pangrama em português, desconsiderando as letras de origem saxônica: 
#Blitz prende ex-vesgo com cheque fajuto.
#Ler um número n, seguido por n frases, uma em cada linha. Para cada frase, escrever "S" ou "N" caso seja pangrama inglês ou não (desconsidera acentos).

def pangrama():
    n = int(input("Digite um número: "))

    for i in range(n):
        frase = str(input(f"Digite a frase {i+1}: ")).lower() #transformando tudo para minúculas 
        letras_na_frase = set(list(frase)) #dividindo as letrinhas
        letras_no_alfabeto = set('abcdefghijklmnopqrstuvwxyz') #digitando todas as letras do alfabeto para comparar 

        if letras_no_alfabeto.issubset(letras_na_frase): #verifica se todas as letras do alfabeto estão presentes na frase 
        #if letras_presentes.issubset(letras_do_alfabeto): verifica se todos os elementos de letras_presentes estão presentes em letras_do_alfabeto (errado)
            print("S")
        else:
            print("N")
        
pangrama()
