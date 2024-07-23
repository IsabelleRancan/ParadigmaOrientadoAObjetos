#Implemente a função contida: Recebe duas strings. Retorna True ou False dependendo se a primeira string possui todos os 
#caracteres da segunda string ou não. 

def contida(palavra1, palavra2):
    entrada1 = set(palavra1)
    entrada2 = set(palavra2)

    if entrada1 == entrada2:
        return ("True")
    else:
        return("False")
    
#TESTE:
    
palavra1 = ("ano")
palavra2 = ("ok")

teste = contida(palavra1, palavra2)
print(teste)