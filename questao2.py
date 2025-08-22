def teste_polindromo(item):
    frase = item.replace(
        " ", ""
    ).lower()  # tratamento de erro para remover espaço em branco e pcaps

    if frase == frase[::-1]:
        print("É Polindromo")
    else:
        print("Não é Polimbromo")


# palavra = input("Digite uma palavra ou frase: ")
palavra = "Socorram me subino onibus em marrocos"
teste_polindromo(palavra)
