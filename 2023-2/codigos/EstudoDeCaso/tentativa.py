class Caixa:
    def __init__(self, interior=[]):
        self.interior = interior

    def insira_sapato(self, s):
        if len(self.interior) >= 2:  # se o array tiver mais que dois elementos dentro, ele n aceita mais nenhum
            print('Caixa cheia')
        else:
            # inserirndo sapato no atributo interior da caixa
            self.interior.append(s)
            print('Sapato inserido')
        print(len(self.interior)) #print a quantidade de itens

class Sapato:
    def __init__(self, t):
        self.tipo = t


caixa_azul = Caixa()
sapato_feio = Sapato('direito')
sapato_feio2 = Sapato('esquerdo')
sapato_feio3 = Sapato('roxo')
caixa_azul.insira_sapato(sapato_feio)
caixa_azul.insira_sapato(sapato_feio2)
caixa_azul.insira_sapato(sapato_feio3)

print(caixa_azul.interior)
