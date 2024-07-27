with open('leia.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

    for numero, linha in enumerate(linhas, start=1):
        print(f"{numero}: {linha.strip()}")

    n_linha = int(input("Digite o número da linha que quer apagar: "))

    if n_linha <1 or n_linha > len(linhas):
        print("Número invalido")
    else: 
        linhas.pop(n_linha - 1)

    with open('leia.txt', 'w') as arquivo: 
        arquivo.writelines(linhas)

    print(f"Nova lista: ")
    for numero, linha in enumerate(linhas, start=1):
        print(f"{numero}: {linha.strip()}")