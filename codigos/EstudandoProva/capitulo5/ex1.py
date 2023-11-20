from urllib.request import urlopen
import time
 
class WebPage:
    def __init__(self, url,cache_timeout=60): 
        "definindo o tempo para 60 segundos"
        self.url = url
        self._content = None
        self._cache_timeout = cache_timeout
        self._ultimo_carregamento = 0 
 
    @property
    def cache_timeout(self):
        "criando um metodo getter para poder exibit o atributo sem chamar o método __init__"
        return self._cache_timeout
    
    @cache_timeout.setter
    def cache_timeout(self, value):
        "criando o método setter para o atributo, isso permite modificar o valor como uma atribuição direta"
        self._cache_timeout = value
   
    @property
    def content(self):
        hora_atual = time.time() #definindo o valor da variável para a hora atual
        if not self._content or (hora_atual - self._ultimo_carregamento) > self._cache_timeout:
            """Em resumo, essa linha verifica se:
                Não há conteúdo em cache (not self._content), ou
                O tempo decorrido desde a última busca excede o tempo limite do cache.
                Se pelo menos uma dessas condições for verdadeira, o bloco de código dentro do if será executado, o que inclui a busca
                de uma nova página (caso necessário) e a atualização do conteúdo e do tempo da última busca."""
            
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self._ultimo_carregamento = hora_atual
        return self._content
    

webpage = WebPage("http://ccphillips.net/")
now = time.time()
content1 = webpage.content
"Retrieving New Page..."
time.time() - now
22.43316888809204
now = time.time()
content2 = webpage.content
time.time() - now
1.9266459941864014
content2 == content1
True