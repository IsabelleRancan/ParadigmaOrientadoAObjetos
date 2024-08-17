#pedir pares de frases para o usuário, para cada par comparar a primeira e segunda frase 
#depois da contagem, verificar quais letras se repetem unicamente e escrever as letras 
#que se repetem em ordem alfabética

#tentando usar uma lista de tuplas

lista_frases = []

while True:
    n_frases = str(input('Digite uma palavra: ')).lower()
    if n_frases == "":
        break;
    else: 
        lista_frases.append(list(n_frases.replace(" ", ""))) #adicionando cada letra como um item de lista e removendo possíveis espaços
print(lista_frases)        

# for frase in lista_frases:
#     retorno = []
#     for p in frase:
#         sliced = p[::-1]
#         retorno.append(sliced)
#         nova_lista = ' '.join(retorno)

#     print(nova_lista)