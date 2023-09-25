class A:
    def mostrar(self):
        print(f'Esse método pertence à classe "A"')

class B(A):
    def mostrar(self):
        super().mostrar()
        #print(f'Esse método pertence à classe "B"')

class C(A):
    def mostrar(self):
        super().mostrar()
        #print(f'Esse método pertence à classe "C"')

class D(B, C):
    pass 

teste = D()
teste.mostrar()