#Ler um número n, seguido por uma sequência de n números. Escrever os números, sem duplicatas, ordenadamente.

def sequencia():
    numeros = set()
    n = int(input())

    for i in range(n):
        numero = int(input())
        numeros.add(numero)

    numeros_ordenados = sorted(numeros)
    print("Numeros ordenados: ", numeros_ordenados)

sequencia()