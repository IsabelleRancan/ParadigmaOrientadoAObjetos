from datetime import datetime
from collections import defaultdict, namedtuple

# Definindo uma namedtuple chamada "InformacaoAcao"
InformacaoAcao = namedtuple('InformacaoAcao', ['data', 'preco_fechamento'])

class BolsaDeValores:
    def __init__(self):
        # Usando defaultdict para lidar com novas entradas automaticamente
        self.acoes = defaultdict(list)

    def add(self, chave, data, preco_fechamento):
        # Convertendo a data para o formato datetime se necessário
        if not isinstance(data, datetime):
            data = datetime.strptime(data, '%d/%m')

        # Criando uma namedtuple e adicionando informações de preço de fechamento
        informacao_acao = InformacaoAcao(data, preco_fechamento)
        self.acoes[chave].append(informacao_acao)

    def get_informacoes_por_chave(self, chave):
        return self.acoes.get(chave, [])

# Exemplo de uso
bolsa = BolsaDeValores()

# Adicionando informações de preço de fechamento para ação 'Google'
bolsa.add('Google', '01/03', 150)
bolsa.add('Google', '02/03', 160)

# Adicionando informações de preço de fechamento para ação 'Facebook'
bolsa.add('Facebook', '01/03', 50)
bolsa.add('Facebook', '02/03', 55)

# Obtendo informações apenas para a chave 'Google'
informacoes_google = bolsa.get_informacoes_por_chave('Google')

# Imprimindo as informações com nomes de campo
for informacao in informacoes_google:
    print(f"Data: {informacao.data.strftime('%d/%m/%Y')}, Preço de Fechamento: {informacao.preco_fechamento}")
        