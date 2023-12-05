class Estudante:

    def __init__(self, nome: str, sobrenome: str, notas: list):
        self._nome = nome
        self._sobrenome = sobrenome
        self._notas = notas

    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @nome.setter  
    def nome(self, novo_nome):
        if novo_nome.isalpha() and novo_nome[0].isupper():
            self._nome = novo_nome
        else:
            raise Exception('TypeError: dado inválido')
        
    @sobrenome.setter  
    def sobrenome(self, novo_sobrenome):
        if novo_sobrenome.isalpha() and novo_sobrenome[0].isupper():
            self._sobrenome = novo_sobrenome  
        else:
            raise Exception('TypeError: dado inválido')  

    @property
    def nome_completo(self):
        return self.nome +  " "  + self.sobrenome #tá sem o sublinhado pq tá retornando o property

    def adicionar_nota(self, nova_nota):
        self._notas.append(nova_nota)

    def excluir_nota(self, indice):
        del self._notas [indice]

    @property
    def notas(self):
        return str(self._notas)

    @property 
    def media(self):
        soma = 0 
        for elemento in self._notas:
            soma += elemento
        return soma / len(self._notas) #utilizando a propriedade length pra contar quantos elementos eu tenho na lista 
    
