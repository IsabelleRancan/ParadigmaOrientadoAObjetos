from auth import * 

class castrandoUsuario(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        try: Authenticator.add_user()
        except: TypeError("Digite apenas letras")
        else: print("Usuário cadastrado com sucesso!")
        finally: ("Usuário cadastrado com sucesso!")
        self.username = username
        self.password = password
        

Usuario1 = castrandoUsuario("Ana", "Anasenha")
