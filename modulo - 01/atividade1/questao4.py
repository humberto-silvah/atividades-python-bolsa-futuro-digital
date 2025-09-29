def verifica_senhas(senha):
    if len(senha) <= 8:
        print("Senha Fraca")
        return

    tem_maiuscula = any(caracter.isupper() for caracter in senha)
    tem_minuscula = any(caracter.islower() for caracter in senha)
    tem_digito = any(caracter.isdigit() for caracter in senha)

    if tem_maiuscula and tem_minuscula and tem_digito:
        print("Senha Forte")
    else:
        print("Senha Fraca")


senha = input("Digite a senha: ")

# senha = "C0digoLegal"
# verifica_senhas(senha)
# senha = "codigo"
verifica_senhas(senha)
