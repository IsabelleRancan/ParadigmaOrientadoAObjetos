from auth import PasswordTooShort, PasswordWithoutLowerCase, PasswordWithoutUpperCase, authenticator

while True:
    nome_usuario = input("digite o nome de usuário: ")
    senha = input("digite a senha: ")

    try:
        usuario = authenticator.add_user(nome_usuario, senha)
        print("Usuário", nome_usuario, "criado com sucesso!")
        break
    except PasswordTooShort:
        print("\nInsira uma senha com pelo menos 6 caracteres!\n")
    except PasswordWithoutLowerCase:
        print("\nInsira uma senha com pelo menos uma letra minúscula!\n")
    except PasswordWithoutUpperCase:
        print("\nInsira uma senha com pelo menos uma letra maiúscula!\n")
