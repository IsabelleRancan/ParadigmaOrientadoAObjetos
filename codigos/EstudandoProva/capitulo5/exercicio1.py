from urllib.request import urlopen
import time
 
class WebPage:
    def __init__(self, url, cache_timeout=20):
        self.url = url
        self._content = None
        self._cache_timeout = cache_timeout
        self.ultimo_carregamento = 0

    @property
    def cache_timeout(self):
        return self._cache_timeout
    
    @cache_timeout.setter
    def cache_timeout(self, valor):
        self._cache_timeout = valor
        print("Tempo alterado com sucesso!")
 
    @property
    def content(self):
        hora_atual = time.time() #atributo que recebe a hora atual (não precisa do self no inicio)
        if not self._content or (hora_atual - self.ultimo_carregamento) > self._cache_timeout:
            print("Recarregando a página...")
            self._content = urlopen(self.url).read()
            self.ultimo_carregamento = hora_atual #o horario fica fixo
        return self._content
    
# Exemplo de uso
webpage = WebPage("https://g1.globo.com/")
webpage.cache_timeout = 60

now = time.time()
content1 = webpage.content
print("Tempo de busca:", time.time() - now)

now = time.time()
content2 = webpage.content
print("Tempo de busca:", time.time() - now)

print("Conteúdos iguais?", content2 == content1)