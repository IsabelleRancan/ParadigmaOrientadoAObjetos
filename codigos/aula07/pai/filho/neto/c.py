#caminho relativo
from ...a import A
from ...b import B

#caminho absoluto
from a import nome_modulo as a_nome_modulo
from filho.b import nome_modulo as b_nome_modulo

C = 3

def nome_modulo():
    print('dentro de ', __name__)

if __name__ == '__main__':
    print(A, B, C)
    a_nome_modulo()
    b_nome_modulo()
    nome_modulo()