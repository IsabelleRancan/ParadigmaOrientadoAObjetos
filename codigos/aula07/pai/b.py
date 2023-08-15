#caminho relativo
from .a import A
from .filho.neto.c import C 

#caminho absoluto
from a import nome_modulo as a_nome_modulo
from filho.neto.c import nome_modulo as c_nome_modulo

B = 20

def nome_modulo():
    print('dentro de ', __name__)

if __name__ == '__main__':
    print(A, B, C)
    a_nome_modulo()
    nome_modulo()
    c_nome_modulo()