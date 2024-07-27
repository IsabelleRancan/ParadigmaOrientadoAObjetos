#ex2 - função contida: Recebe duas strings. Retorna True ou False dependendo se a primeira string possui todos os caracteres da segunda string ou não

def contida(p1, p2): 
    s1 = set(p1)
    s2 = set(p2)
    return s1.issubset(s2)

#EXERCÍCIO 2 
print(contida("abc", "abcdef"))  # Esperado: True
print(contida("abc", "def"))     # Esperado: False
print(contida("aab", "ab"))      # Esperado: True
print(contida("aab", "aa")) 