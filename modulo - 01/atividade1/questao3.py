def verequencia_palavras(frase):
    palavras = frase.split()
    frequencia = {}  # Cria um dicionário para armazenar a contagem

    # Percorre cada palavra e atualiza a contagem
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    for palavra, contagem in frequencia.items():  # Exibe o resultado
        print(f"{palavra}: {contagem}")


frase = "eu gosto de python e eu gosto de programar"
# frase =input("Digite a frase: ")


verequencia_palavras(frase)
