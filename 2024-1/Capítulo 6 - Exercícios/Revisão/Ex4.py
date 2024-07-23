#Escreva um programa que solicita ao usuário uma frase e retorna o número de vogais na frase.

def n_vogais():
    vogais = 'aeiuo'

    frase = str(input("Digite uma frase: ")).lower
    frase = frase.replace(" ", "")
    frase = list(frase)