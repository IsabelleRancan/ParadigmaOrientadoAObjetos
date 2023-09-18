class Pizza:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
 
    @classmethod
    def marguerita(cls):
        return cls(["molho de tomate", "manjericão", "rodelas de tomate fresco", "azeitona", "queijo muçarela", "orégano salpicado"])
 
    @classmethod
    def calabresa(cls):
        return cls(["queijo", "molho de tomate", "calabresa em rodelas", "cebola", "tomate picado", "azeite", "orégano"])
 
 
p1 = Pizza(["queijo", "azeitona preta", "ovo cozido", "presunto cozido", "cebola", "ervilha", "molho de tomate", "azeite"])
p2 = Pizza.marguerita()
p3 = Pizza.calabresa()
 
print("\nPizza de Portuguesa:", p1.ingredientes)
print("\nPizza de Marguerita:", p2.ingredientes)
print("\nPizza de Calabresa:", p3.ingredientes)
