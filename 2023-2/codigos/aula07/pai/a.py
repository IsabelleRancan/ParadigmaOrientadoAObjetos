#caminho relativo
from.b import b
from.filho.neto.c import c

#caminho absoluto
from filho.b import nome_modulo as b_nome_modulo
from filho.neto.c import nome_modulo as c_nome_modulo

A = 10

def nome_modulo():
    print('dentro de ', __name__)

#verificando se é o módulo principal ou não
if __name__ == '__main__':
    print(A, B, C)
    nome_modulo()
    b_nome_modulo()
    c_nome_modulo()
