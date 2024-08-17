lista_frases = []

while True:
    n_frases = str(input('Digite uma frase: '))
    if n_frases == "":
        break;
    else: 
        lista_frases.append(n_frases.split())

for frase in lista_frases:
    retorno = []
    for p in frase:
        sliced = p[::-1]
        retorno.append(sliced)
        nova_lista = ' '.join(retorno)

    print(nova_lista)