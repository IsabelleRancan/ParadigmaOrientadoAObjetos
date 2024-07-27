def combinar_listas(lista1, lista2):
    l1 = lista1
    l2 = lista2 

    if len(l1) != len(l2):
        raise ValueError ("As listas possuem tamanhos diferentes!")
    
    return list(zip(l1, l2)) 

def contida(string1, string2):
    s1 = set(string1)
    s2 = set(string2)

    return s1.issubset(s2)





#EX1
teste = combinar_listas(["ana", "banana"], [1, 2])
print(teste)

try: 
    teste2 = combinar_listas(["ana", "banana", "joana"], [1, 2])
    print(teste)
except ValueError as e:
    print(e)


#EX2
cont = contida('12345', '123456')
print(cont)
