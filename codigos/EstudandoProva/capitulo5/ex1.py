from urllib.request import urlopen
from datetime import datetime, timedelta
import time
 
class WebPage:
    def __init__(self, url, cache_timeout):
        self.url = url
        self._content = None

        self.cache_timeout 
 
    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content
    
    
    @property
    def timeout(self):
        

import time
webpage = WebPage("https://www.uol.com.br/splash/")
now = time.time()
content1 = webpage.content
print ("Retrieving New Page...")
time.time() - now
22.43316888809204
now = time.time()
content2 = webpage.content
time.time() - now
1.9266459941864014
content2 == content1
True