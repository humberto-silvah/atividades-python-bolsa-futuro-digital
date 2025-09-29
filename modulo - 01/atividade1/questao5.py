def gerar_acronimo(frase):
    stopwords = ["de", "da", "do", "das", "dos", "e"]
    palavras = frase.split()

    letras = [
        palavra[0].upper() for palavra in palavras if palavra.lower() not in stopwords
    ]

    # Junta tudo em uma string
    acronimo = "".join(letras)

    print("Acrônimo:", acronimo)


# entrada = input("Digite o nome do curso/expressão: ")

entrada = "linguagens de programação e estruturas de Dados"
gerar_acronimo(entrada)
