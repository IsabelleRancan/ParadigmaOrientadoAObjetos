# 1. Lê o caminho para um arquivo de texto.
# 2. Abre o arquivo especificado e escreve seu conteúdo na tela, enumerando cada linha.
# 3. Lê o número da linha a ser removida do arquivo.
# 4. Remove a linha selecionada do arquivo.
# 5. Salva o arquivo atualizado, agora sem a linha removida.
# Dicas:
# ➢ Utilize a função open para abrir o arquivo.
# ➢ Utilize o método readlines para ler todas as linhas do arquivo.
# ➢ Ao exibir as linhas enumeradas, você pode utilizar um contador para acompanhar o número da linha.
# ➢ Para remover a linha selecionada, você pode utiliza

with open('leia.txt', 'r') as arquivo:
    conteudo = arquivo.readlines() #conteudo é uma lista e arquivo é o objeto, meio que o conteúdo em si 

    for numero, linha in enumerate(conteudo, start=1):
        print(f"{numero} : {linha.strip()}")

    n_linha = int(input("Digite o número da linha que deseja apagar: "))

    if n_linha <1 or n_linha > len(conteudo):
        print("Número inválido!")

    else: 
        conteudo.pop(n_linha - 1)
        with open('leia.txt', 'w') as arquivo:
            arquivo.writelines(conteudo)

            print("Lista Atualizada: ")
            for numero, linha in enumerate(conteudo, start=1):
                print(f"{numero}: {linha.strip()}")

