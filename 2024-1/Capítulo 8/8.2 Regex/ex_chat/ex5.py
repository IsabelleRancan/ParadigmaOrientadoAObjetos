# validar senhas
import re 

senha = "Senha@123"
senha2 = "senha123"

def senha_correta():
    return bool(re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*])[A-Za-z\d@#$%^&*]{8,}$", senha2))

print(senha_correta())