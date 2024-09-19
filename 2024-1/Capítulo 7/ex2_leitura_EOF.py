import sys

nome_arquivo = input("Digite o nome do arquivo (com extensão): ")

try:
    # Tenta abrir o arquivo no modo 'x', que cria o arquivo, mas levanta um erro se ele já existir
    with open(nome_arquivo, 'x') as arquivo:
        print("Digite o texto. Para encerrar, pressione Ctrl+Z (no Windows) ou Ctrl+D (no Linux/Mac) para finalizar.")

        texto = sys.stdin.read()  # Ler até EOF (Ctrl+Z ou Ctrl+D)
        arquivo.write(texto)

    print(f"O texto foi salvo em {nome_arquivo}.")
    
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(f"\n{conteudo}" ) 

except FileExistsError:
    print(f"O arquivo '{nome_arquivo}' já existe. Escolha outro nome.")
